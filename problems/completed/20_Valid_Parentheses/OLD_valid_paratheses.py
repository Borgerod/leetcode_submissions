class Solution:
    def isValid(self, s: str) -> bool:
        # SOLUTION WITH STACKS 
        stack = []
        lookup = {
            ")":"(",
            "]":"[",
            "}":"{",
        }
        for p in s:
        
            if p in lookup.values():
                stack.append(p)

            elif stack and lookup[p] == stack[-1]: #there is items in stack, and the last item in stack == the value of "p" 
                stack.pop() #we then temove the valid parenthesis from stack #! important 
                #if not the formula wont work on nested parenthesis that closes before the parent closes .e.g. (( [] {} ))
            
            else:  #stack is empty, or the last item in stack != the value of "p" 
                return False
        
        return stack == []
            
      
'''MY SOLUTION WITHOUT STACKS'''
    # def isValid(self, s: str) -> bool:
    #     opposite = {
    #         "(":")",
    #         "[":"]",
    #         "{":"}",
    #     }
    #     expectations = []
    #     order =[]
    #     for i in range(0,len(s)):
    #         if i+1 > len(s):
    #             break
    #         if s[i] not in opposite.keys():
    #             if not expectations or s[i] != expectations[-1]:
    #                 return False
    #             else:
    #                 expectations.pop(-1)
    #                 order.pop(-1)
    #         if s[i] in opposite.keys():
    #             expectations.append(opposite[s[i]])
    #             order.append(s[i])
    #     return not order or not expectations or order == expectations
      
if __name__ == '__main__':
    for case in [
        "()",
        "()[]{}",
        "(]",
        "(([]{}))",
        "(())",
    ]: print(Solution().isValid(case))

