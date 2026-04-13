
# ORIGINAL SOLIUTION
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for i in s:
            print(f"char: '{i}'" )
            if i in closeToOpen:
                while stack and stack[-1] == closeToOpen[i]:
                    print(f"    close:           {stack} -> '{i}'")
                    stack.pop()
                    break
                else: 
                    print("invalid detedcted => false")
                    return False
            else:
                print(f"    append: '{i}' -> {stack}")
                stack.append(i)

        print(f"\nfinal stack: {stack}")            
        return not stack #->true if empty
    
# CLEAN VERSION 
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for i in s:
            if i in closeToOpen:
                while stack and stack[-1] == closeToOpen[i]:
                    stack.pop()
                    break
                else: 
                    return False
            else:
                stack.append(i)
        return not stack #->true if empty
        
# SIMPLIFIED
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        for i in s:
            if i in closeToOpen:
                if not stack or stack[-1] != closeToOpen[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return not stack


if __name__ == '__main__':

    cases = [
        "(])",       #False
        "[[[]",     #False
        "(",        #False
        "]",        #False
        "()",       #True
		"()[]{}",   #True    
		"(]",       #False
		"([])",     #True
    ]
    fasit = [
        False,
        False,
        False,
        False,
        True,
        True,
        False,
        True,
    ]
    #> OPTION 1 (for single inputs)
    s = Solution()
    for i, case in enumerate(cases):
        print(f"___ NO.{i} ___________________________________")
        print(f"n={i} -> {s.isValid(case)}  => [{'Correct' if s.isValid(case)==fasit[i] else 'X'}] {'' if s.isValid(case)==fasit[i] else f'(fasit: {fasit[i]})'} \n")



