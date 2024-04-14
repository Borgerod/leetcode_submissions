class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        return ""
  






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