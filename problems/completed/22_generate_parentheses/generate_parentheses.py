class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        '''
        Gave up, working from solutions
        '''
        def builder(left, right, current_string):
            left:int = current_string.count("(")
            right:int = current_string.count(")")

            
            if len(current_string) == string_limit:
                string_alternatives.append(current_string)
                return

            if left < n:
                builder(left, right, current_string+'(')

            if right < left:
                builder(left, right, current_string+')')

        string_alternatives:list[str] = []
        string_limit:int = n*2 #[TEMP]
        current_string:str = "" #stack

        builder(0, 0, current_string)
        return  list(set(string_alternatives))
    
def main():
    '''
        Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
        
        Example 1:

            Input: n = 3
            Output: [((())),(()()),(())(),()(()),()()()]
        Example 2:

            Input: n = 1
            Output: [()]

        Constraints: 1 <= n <= 8
    '''

    testcases = [
        3,
        1, 
        8,
    ]
    s = Solution()
    for n in testcases:
        res = s.generateParenthesis(n)
        print(res)

if __name__ == '__main__':
    main()

'''
    1: ()
    2: ()(), (()), 
    3: ()()(), (())(), ()(()), ((())), (()())
    4: ()()()(), (())()(), ()()(()), (())(()), (((()))), (()()()), ((())()), (()(()))
'''