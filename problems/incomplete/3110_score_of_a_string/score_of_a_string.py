class Solution:
    #SOL 1.0) Quick and Easy, how can i do it better? (optimize)
    def scoreOfString(self, s: str) -> int:
        sum_ascii = 0
        i=0
        while i < len(s)-1:
            a = ord(s[i])
            b = ord(s[i+1])
            print( f"i:{i}/{len(s)-1} | a-b: {a}-{b}: {a-b} --> positive convertion: {abs(a-b)}")
            sum_ascii += abs(s[i]-s[i+1])
            i+=1
        return sum_ascii
    
    #SOL 1.1) Cleaned up 
    #> (SHOULD BE THE FASTEST)
    def scoreOfString(self, s: str) -> int:
        sum_ascii,i = 0,0
        while i < len(s)-1: sum_ascii += abs(ord(s[i])-ord(s[i+1])); i+=1
        return (sum_ascii)
    
    #SOL 2.0.) for loop
    def scoreOfString(self, s: str) -> int:
        sum_ascii,a,b,i = 0,0,0,0
        a = s[0]
        for i in s[1:]:
            b = i
            sum_ascii += abs(ord(a)-ord(b))
            a = b
        return sum_ascii
    
    #SOL 2.1) compressed 
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(s[i])-ord(s[i+1])) for i in range(len(s)-1))

'''
NOTE: 
    "w a l l"
    [w-a][a-l][l-l][l-?]
    even numbers does not matter 
'''


if __name__ == '__main__':

    cases = [

        "hello",
        "zaz",
        "wall",
        "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqr",
        "zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlk",

    ]
    # > OPTION 1 (for single inputs)
    S = Solution()
    for i, s in enumerate(cases):
        print(f"___ NO.{i} ___________________________________")
        print(f"n={i} -> {S.scoreOfString(s)}\n")





'''
expected outputs: 
    1: 13
    2: 50
'''