import os
import re
import sys
import json
import requests
from html.parser import HTMLParser

class HTMLFilter(HTMLParser):
    """Remove HTML tags from description"""
    text = ""
    def handle_data(self, data):
        self.text += data
    def handle_starttag(self, tag, attrs):
        if tag == 'br':
            self.text += '\n'
        elif tag in ['p', 'div']:
            self.text += '\n'
    def handle_endtag(self, tag):
        if tag in ['p', 'div']:
            self.text += '\n'

def clean_html(html_text):
    """Remove HTML tags from description and format nicely"""
    f = HTMLFilter()
    f.feed(html_text)
    text = f.text.strip()
    
    # Clean up excessive whitespace and format properly
    lines = text.split('\n')
    formatted_lines = []
    in_example = False
    in_constraints = False
    
    def wrap_text(text, width=100, indent_level=0):
        """Wrap text to specified width with optional indentation"""
        if not text.strip():
            return ['']
        
        words = text.split()
        lines = []
        current_line = ''
        indent = '    ' * indent_level
        
        for word in words:
            # Check if adding this word would exceed the width
            test_line = current_line + (' ' if current_line else '') + word
            if len(indent + test_line) <= width:
                current_line = test_line
            else:
                # Start a new line
                if current_line:
                    lines.append(indent + current_line)
                current_line = word
        
        # Add the last line
        if current_line:
            lines.append(indent + current_line)
        
        return lines if lines else ['']
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        if not line:  # Empty line
            formatted_lines.append('')
            continue
            
        # Check if we're starting an example or constraints section
        if line.startswith('Example ') and line.endswith(':'):
            in_example = True
            in_constraints = False
            formatted_lines.append(line)
            continue
        elif line.lower().startswith('constraint') and ':' in line:
            in_example = False
            in_constraints = True
            formatted_lines.append(line)
            continue
            
        # Handle Input/Output/Explanation lines (always indent these)
        if line.startswith(('Input:', 'Output:', 'Explanation:')):
            formatted_lines.append(f'    {line}')
            continue
            
        # Skip pure number lines
        if line.replace(' ', '').replace('\t', '').isdigit():
            continue
            
        # Handle content based on current section
        if in_example:
            # In example section - indent everything except the Example X: header
            if not (line.startswith('Example ') and line.endswith(':')):
                # For example content, wrap with 1 level of indentation
                wrapped = wrap_text(line, width=100, indent_level=1)
                formatted_lines.extend(wrapped)
            else:
                formatted_lines.append(line)
        elif in_constraints:
            # In constraints section - indent all constraint details
            wrapped = wrap_text(line, width=100, indent_level=1)
            formatted_lines.extend(wrapped)
        else:
            # Regular content outside examples/constraints - wrap to full width
            wrapped = wrap_text(line, width=100, indent_level=0)
            formatted_lines.extend(wrapped)
    
    # Remove excessive empty lines (max 1 consecutive for cleaner look)
    final_lines = []
    empty_count = 0
    
    for line in formatted_lines:
        if not line.strip():
            empty_count += 1
            if empty_count <= 1:  # Only allow 1 consecutive empty line
                final_lines.append(line)
        else:
            empty_count = 0
            final_lines.append(line)
    
    return '\n'.join(final_lines)

def get_vscode_settings():
    """Get VS Code indentation settings"""
    settings = {
        'insert_spaces': True,  # Default to spaces
        'tab_size': 4,         # Default to 4 spaces
        'indent_string': '    ' # Default indent
    }
    
    # Try to read workspace settings first
    workspace_settings_path = os.path.join('.vscode', 'settings.json')
    user_settings_path = os.path.expanduser('~/AppData/Roaming/Code/User/settings.json')
    
    def read_settings_file(path):
        """Read and parse settings JSON file"""
        try:
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Remove comments (simple approach)
                    lines = content.split('\n')
                    clean_lines = []
                    for line in lines:
                        # Remove // comments
                        if '//' in line:
                            line = line[:line.index('//')]
                        clean_lines.append(line)
                    clean_content = '\n'.join(clean_lines)
                    return json.loads(clean_content)
        except (json.JSONDecodeError, FileNotFoundError, PermissionError):
            pass
        return {}
    
    # Read workspace settings (takes priority)
    workspace_settings = read_settings_file(workspace_settings_path)
    
    # Read user settings (fallback)
    user_settings = read_settings_file(user_settings_path)
    
    # Merge settings (workspace overrides user)
    all_settings = {**user_settings, **workspace_settings}
    
    # Extract relevant settings
    if 'editor.insertSpaces' in all_settings:
        settings['insert_spaces'] = all_settings['editor.insertSpaces']
    
    if 'editor.tabSize' in all_settings:
        settings['tab_size'] = all_settings['editor.tabSize']
    
    # Check for Python-specific settings
    python_settings = all_settings.get('[python]', {})
    if 'editor.insertSpaces' in python_settings:
        settings['insert_spaces'] = python_settings['editor.insertSpaces']
    if 'editor.tabSize' in python_settings:
        settings['tab_size'] = python_settings['editor.tabSize']
    
    # Create indent string
    if settings['insert_spaces']:
        settings['indent_string'] = ' ' * settings['tab_size']
    else:
        settings['indent_string'] = '\t'
    
    return settings

def fetch_leetcode_problem(problem_slug):
    """Fetch problem data using LeetCode's GraphQL API"""
    
    url = "https://leetcode.com/graphql"
    
    # GraphQL query
    query = """
    query getQuestionDetail($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            questionFrontendId
            title
            titleSlug
            difficulty
            content
            topicTags {
                name
                slug
            }
            codeSnippets {
                lang
                code
            }
            exampleTestcases
        }
    }
    """
    
    variables = {"titleSlug": problem_slug}
    
    headers = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com"
    }
    
    try:
        response = requests.post(url, json={"query": query, "variables": variables}, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        if 'errors' in data:
            print(f"API Error: {data['errors']}")
            return None
            
        question = data['data']['question']
        
        # Get Python code snippet
        python_code = None
        for snippet in question['codeSnippets']:
            if snippet['lang'] == 'Python3':
                python_code = snippet['code']
                break
        
        if not python_code:
            print("No Python3 code snippet found")
            return None
        
        # Fix capitalized types (List[str] -> list[str])
        python_code = re.sub(r'\bList\[', 'list[', python_code)
        python_code = re.sub(r'\bDict\[', 'dict[', python_code)
        python_code = re.sub(r'\bSet\[', 'set[', python_code)
        python_code = re.sub(r'\bTuple\[', 'tuple[', python_code)
        
        # Parse function signature
        func_match = re.search(r'def\s+(\w+)\s*\(self(?:,\s*(.+?))?\)\s*->', python_code, re.DOTALL)
        function_name = func_match.group(1) if func_match else "INSERT_FUNCTION_NAME"
        
        params = []
        if func_match and func_match.group(2):
            param_text = func_match.group(2)
            # Split by comma and extract parameter names
            for param in param_text.split(','):
                param_name = param.split(':')[0].strip()
                if param_name and param_name != 'self':
                    params.append(param_name)
        
        # Parse test cases
        test_cases = question['exampleTestcases'].split('\n') if question['exampleTestcases'] else []
        
        return {
            'number': question['questionFrontendId'],
            'title': f"{question['questionFrontendId']}. {question['title']}",
            'difficulty': question['difficulty'],
            'topics': [tag['name'] for tag in question['topicTags']],
            'description': question['content'],
            'function_name': function_name,
            'params': params,
            'test_cases': test_cases,
            'code_snippet': python_code
        }
        
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def create_files(data):
    """Create folder structure and files with API data"""
    
    # Get VS Code indentation settings
    vscode_settings = get_vscode_settings()
    indent = vscode_settings['indent_string']
    
    print(f"Using indentation: {'spaces' if vscode_settings['insert_spaces'] else 'tabs'} "
          f"(size: {vscode_settings['tab_size']})")
    
    # Create folder name: "2942_Find_Words_Containing_Character"
    folder_name = data['title'].replace(' ', '_').replace('.', '')
    
    # Create file name: "find_words_containing_character.py"
    title_without_number = re.sub(r'^\d+\s*\.?\s*', '', data['title'])
    file_name = title_without_number.replace(' ', '_').lower() + '.py'
    
    # Create folder path
    base_path = os.path.join('problems', 'incomplete', folder_name)
    os.makedirs(base_path, exist_ok=True)
    
    # Create description.txt
    desc_path = os.path.join(base_path, 'description.txt')
    
    # Create matching underlines
    title_line = f"___ {data['title']} "
    total_width = 100  # Target total width
    remaining_width = total_width - len(title_line)
    title_underline = '_' * max(0, remaining_width)
    bottom_underline = '_' * total_width
    
    desc_content = f"""{title_line}{title_underline}
difficulty: {data['difficulty']}
topics: {', '.join(data['topics'])}
{bottom_underline}


{clean_html(data['description'])}
"""
    
    with open(desc_path, 'w', encoding='utf-8') as f:
        f.write(desc_content)
    
    # Create Python file
    py_path = os.path.join(base_path, file_name)
    
    # Build test cases string
    cases_str = ',\n\t\t'.join([f'{case}' for case in data['test_cases']])
    if not cases_str:
        cases_str = '"TESTCASE"'
    
    # Choose boilerplate based on number of parameters
    if len(data['params']) <= 1:
        param_name = data['params'][0] if data['params'] else 'PARAM'
        bottom_boilerplate = f'''
{indent}#> OPTION 1 (for single inputs)
{indent}s = Solution()
{indent}for i, {param_name} in enumerate(cases):
{indent}{indent}print(f"___ NO.{{i}} ___________________________________")
{indent}{indent}print(f"n={{i}} -> {{s.{data['function_name']}({param_name})}}\\n")
'''
    else:
        param_list = ', '.join(data['params'])
        bottom_boilerplate = f'''
{indent}#> OPTION 2 (for multiple inputs)
{indent}s = Solution()
{indent}for i in range(0, len(cases), {len(data['params'])}):
'''
        for j, param in enumerate(data['params']):
            bottom_boilerplate += f'\n{indent}{indent}{param} = cases[i+{j}]'
        bottom_boilerplate += f'''
{indent}{indent}print(f"___ NO.{{i}} ___________________________________")
{indent}{indent}print(f"n={{i}} -> {{s.{data['function_name']}({param_list})}}\\n")
'''
    
    py_content = f'''{data['code_snippet']}
{indent}{indent}\'\'\'
{indent}{indent}
{indent}{indent}\'\'\'



{indent}{indent}return None



{indent}

if __name__ == '__main__':

{indent}cases = [
{indent}{indent}{cases_str}
{indent}]
{bottom_boilerplate}
'''
    
    with open(py_path, 'w', encoding='utf-8') as f:
        f.write(py_content)
    
    print(f"✓ Created folder: {folder_name}")
    print(f"✓ Created files:")
    print(f"  - {desc_path}")
    print(f"  - {py_path}")
    print(f"\nTitle: {data['title']}")
    print(f"Difficulty: {data['difficulty']}")
    print(f"Topics: {', '.join(data['topics'])}")
    print(f"Function: {data['function_name']}")
    print(f"Parameters: {', '.join(data['params'])}")
    
    return base_path

if __name__ == '__main__':
    if len(sys.argv) < 2:
        url_or_slug = input("Enter LeetCode problem URL or slug: ")
    else:
        url_or_slug = sys.argv[1]
    
    # Extract slug from URL if needed
    if 'leetcode.com' in url_or_slug:
        slug_match = re.search(r'/problems/([^/]+)', url_or_slug)
        problem_slug = slug_match.group(1) if slug_match else url_or_slug
    else:
        problem_slug = url_or_slug
    
    print(f"Fetching problem: {problem_slug}...")
    data = fetch_leetcode_problem(problem_slug)
    
    if data:
        base_path = create_files(data)
        print(f"\nFolder succsessfully generated!\n    Folder is located at: {base_path}\n")
    else:
        print("Failed to fetch problem data")