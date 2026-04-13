class Solution(object):
    def strongPasswordChecker(self, password):
        """
        :type password: str
        :rtype: int
        """
        



'''
assumptoin: 
    needs to be built like a sorting algo, 
    as in it needs an score system.

TODO :
    - [ ] make checker for double letters 
          - if passord[x]==password[x+1]
    - [ ] make checker if password contains 'small, big, numbers, special letters'
    - [ ] make exclution list that will return an error message e.g.: [ '!','.',':',]
    - [ ] set limit to password length 
    - [ ] finally make password input 
'''



def checkConsecutiveCharacters(lst):
    if len(set(lst)) == len(lst):
        print(True)
    else:
        print(False)

def checkLength(length):
    if 6<length<20:
        print(True)
        return checkConsecutiveCharacters(getPassword())
    else:
        print("Error: password does not have the correct length")          # return something()

def getPasswordAsList():
    return list(getPassword())

def getLength():
    return len(getPasswordAsList())

def getPassword():
    ''' 
        will be replaved by user input
    '''
    return 'u0020World'

def main():

    checkLength(getLength()) 
    # lst = list(password)
    # length = len(lst)
        
        # Solution.strongPasswordChecker()
         

if __name__ == '__main__':
    main()
