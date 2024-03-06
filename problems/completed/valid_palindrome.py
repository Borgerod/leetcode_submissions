'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric (not numbers and letters) characters, 
it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

TASK: Given a string s, return true if it is a palindrome, or false otherwise.
'''
import re 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]+', '', s).lower() 
        len_s = len(s)

        if (len_s % 2) == 1:
            adj_s = int(len_s/2-0.5)
            s = s[:adj_s]+s[adj_s+1:]
            if len(s) < 1:
                return True

        for i in range(0, len_s):  
            _i = -(i+1)             
            if i > len_s/2:         
                break
            if s[i] != s[_i]:       
                return False
        return True







""" LONGER SOLUTION
import re 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        will iterate through list from both ends; [0:] and [-1:]
        if mismatch was found; return false and break
        else, it will return True. 
        '''
        s = self.stripString(s)
        len_s = len(s)

        if (len_s % 2) == 1: #check for odds:
            s = s[:int(len_s/2-0.5)]+s[int(len_s/2+0.5):] #removes oddity and updates len_s, then continues 
            len_s = len(s)
            if len_s < 1:   #will break and return True if len_s == 1 or empty. 
                return True

        for i in range(0, len_s):   #iterates string and check matches
            _i = -(i+1)             #inverted i
            if i > len_s/2:         #stops halfway
                break
            if s[i] != s[_i]:       # stops when char doesn't macth counterpart
                return False
        return True
            
    def stripString(self, s:str) -> str:
        ''' removes non-alphamumeric chars from str '''
        return re.sub(r'[^a-zA-Z0-9]+', '', s).lower() #removes all but a-z, A-Z and 0-9, then makes lowercase
        # return re.sub(r'\W+', '', s).lower() #removed since "_" is apparently alphanumeric



"""






class Input:

    def getInput(self):# -> list[int, list[int]]:
        return [
            "ab_a",
            "ab-a",
            "AA",
            "A man, a plan, a canal: Panama",
            "race a car",
            "a",
        ]

def main():
    I = Input()
    s = Solution()
    for i in I.getInput():
        result = s.isPalindrome(i)
        print(result)
        print("-"*20)
        

if __name__ == '__main__':
    main()