import random
import string
class Solution:

    def __init__(self):
        # # restrictions checklist
        # self.hasLower:bool = True
        # self.hasUpper:bool = True
        # self.hasDigit:bool = True
        # self.hasSpecial:bool = True
        # self.withinLength:bool = True
        # self.notRepeat:bool = True
        self.hasLower:bool = False
        self.hasUpper:bool = False
        self.hasDigit:bool = False
        self.hasSpecial:bool = False
        self.withinLength:bool = False
        self.notRepeat:bool = True

        # overall checkValue: 
        self.strong:bool=None

        self.repeatStack=[]

    def checkLength(self, length):
        self.withinLength = length in range(6, 21)
        return self.withinLength

    def resetCritera(self):
        # restrictions checklist
        self.hasLower:bool = False
        self.hasUpper:bool = False
        
        self.hasDigit:bool = False
        self.hasSpecial:bool = False
        
        self.withinLength:bool = False

        self.notRepeat:bool = True

        # overall checkValue: 
        self.strong:bool=None

        self.repeatStack=[]

    def criteria(self) -> bool:
        return all(getattr(self, attr) for attr in (
            "hasLower", "hasUpper", "hasDigit", 
            "hasSpecial", 
            "notRepeat"  # <-- This is False, so all() returns False
        ))

   
    
    def getFirstMissingCriteria(self) -> str|None:
        missing_list = []
        
        if not self.hasLower:
            missing_list.append(("lower", random.choice(string.ascii_lowercase)))
        if not self.hasUpper:
            missing_list.append(("upper", random.choice(string.ascii_uppercase)))
        if not self.hasDigit:
            missing_list.append(("digit", random.choice(string.digits)))
        if not self.hasSpecial:
            missing_list.append(("special", random.choice(string.punctuation)))
        
        if missing_list:
            return random.choice(missing_list)[1]
        
        return random.choice(string.ascii_letters)
    
    def peakCritera(self):
        print( 
            '   isStrong result: ',
            {attr: getattr(self, attr) for attr in (
            "hasLower", "hasUpper", "hasDigit", 
            "hasSpecial", 
            "withinLength", 
            "notRepeat"
        )})
  
    def checkRepeat(self, char) -> bool:
        while self.repeatStack and self.repeatStack[-1] != char:
            self.repeatStack.clear()
            # print(f"        New char '{char}' -> clearing stack")
        self.repeatStack.append(char)
        # print(f"    append '{char}' -> {self.repeatStack}\n")
        if len(self.repeatStack) >= 3:
            # print("     *Broke repetition criteria -> return False")
            return False
        return True
    
    def isStrong(self, password:str) -> bool:  #verifyPassWordCriteria
        '''
            returns false if not all criterias are met
        '''  
        # if not self.checkLength(len(password)): return False 
        # print(f"password: {password}")

        self.checkLength(len(password))

        password_so_far = ""
        for char in password:
            # print(f"    checking char: {char}")
            
            if not self.hasUpper and char.isupper():
                # print(f"        * {char} -> isUpper: {char.isupper()}")
                self.hasUpper = True
        
            if not self.hasLower and char.islower():
                # print(f"        * {char} -> isLower: {char.islower()}")
                self.hasLower = True
            
            
            if not self.hasDigit and char.isnumeric():
                # print(f"        * {char} -> isDigit: {char.isnumeric()}")
                self.hasDigit = True
                
            
            if not self.hasSpecial and not char.isalnum(): 
                # print(f"        * {char} -> isSpecial: {not char.isalnum()}")
                self.hasSpecial = True

            if self.notRepeat:
                self.notRepeat = self.checkRepeat(char, password_so_far)
            
            password_so_far += char
        # return self.criteria(True)
        return self.criteria()
    def changeChar(self, char):
        missing = self.getFirstMissingCriteria()
        print("missing: ",  missing)
        return missing

    def checkRepeat(self, char: str, password_so_far: str) -> bool:
        if len(password_so_far) >= 2 and password_so_far[-1] == char and password_so_far[-2] == char:
            return False
        return True

    def remove_from_repetitions(self, password: str, removes_needed: int) -> str:
        password_list = list(password)
        i = 0
        removed = 0
        
        while removed < removes_needed and i < len(password_list):
            j = i
            while j < len(password_list) and password_list[j] == password_list[i]:
                j += 1
            
            rep_len = j - i
            if rep_len >= 3:
                chars_to_remove = min(rep_len % 3 if rep_len % 3 != 0 else 1, removes_needed - removed)
                for _ in range(chars_to_remove):
                    password_list.pop(i)
                    removed += 1
                i += max(0, rep_len - chars_to_remove - 2)
            else:
                i = j
        
        while removed < removes_needed:
            password_list.pop(0)
            removed += 1
        
        return ''.join(password_list)

    def strongPasswordChecker(self, password: str) -> int:
        
        '''
        '''    
        print("orignal password: ", password)
        # self.isStrong(password)
        # self.peakCritera()
        # password = list(password)
         
        # if self.isStrong(password): # STEP 1: CHECK if strong
        #     print("STRONG, HE WILL BE A SOLDIER")
        #     self.peakCritera()
        #     return 0 
        # else: # STEP 2: MAKE strong
        #     print("Error: password NOT strong -> start edit:")
        #     self.peakCritera()
        #     steps:int = 0 #counter
        #     pStack:list[str]=[]
        #     ''' return X steps to make it strong '''
        #     # self.resetCritera()
        #     # self.peakCritera()
        #     print()
        #         # print(f"    checking char: {char}")
            # while not self.isStrong(pStack) and len(pStack) < 20:
            
            
            # while not self.isStrong(pStack) or not 6 <= len(pStack) <= 20:

            #     for char in password:
            #         if len(pStack)==20 and self.criteria:
            #             len(list(password))
            #             len(pStack)
            #             # print("steps before: ", steps)
            #             # _steps = 0 
            #             # _steps += len(list(password))-len(pStack)
            #             # steps += len(password)
            #             # print("steps after: ", steps)
            #             # print("other :steps: ", _steps)

            #             break
            
            #         # if not self.hasUpper and
            #         if char.isupper():
            #             print(f"        * {char} -> isUpper: {char.isupper()}")
            #             self.hasUpper = True
            #             pStack.append(char)
            #             password.pop(0)
            #             steps +=1
            #             # continue
                
            #         # if not self.hasLower and
            #         if char.islower():
            #             print(f"        * {char} -> isLower: {char.islower()}")
            #             self.hasLower = True
            #             pStack.append(char)
            #             password.pop(0)
            #             steps +=1
            #             # continue
                    
                    
            #         # if not self.hasDigit and
            #         if char.isnumeric():
            #             print(f"        * {char} -> isDigit: {char.isnumeric()}")
            #             self.hasDigit = True
            #             print(f"pstack append char: {char}")
            #             # print("before: ", password)
            #             pStack.append(char)
            #             password.pop(0)
            #             # print("after: ", password)
            #             steps +=1
            #             # continue
                        
                    
            #         # if not self.hasSpecial and
            #         if not char.isalnum(): 
            #             print(f"        * {char} -> isSpecial: {not char.isalnum()}")
            #             self.hasSpecial = True
            #             pStack.append(char)
            #             password.pop(0)
            #             # continue

            #         if self.notRepeat:
            #             self.notRepeat = self.checkRepeat(char)

                    
            #     # print(f"pStack: {pStack}")

            #     print("pStack: " + "".join(pStack))
            #     print(f"len_pStsack: {len(pStack)}")
            #     print(f"steps: {steps}")

        original_password = len(password)
        self.resetCritera()
        steps = 0
        # while not self.isStrong(password) or not 6 <= len(password) <= 20:
        #     self.resetCritera()
        #     newPassword = ""
        #     for char in password:
        #         if not self.checkRepeat(char):
        #             new_char = self.changeChar(char)
        #             steps += 1
        #             newPassword += new_char
        #         else:
        #             if char.isupper():
        #                 if self.hasUpper:
        #                     print(f"skip {char}")
        #                 else:
        #                     print(f"make step {char}")
        #                     self.hasUpper = True
        #                 newPassword += char
        #             elif char.islower():
        #                 if self.hasLower:
        #                     print(f"skip {char}")
        #                 else:
        #                     print(f"make step {char}")
        #                     self.hasLower = True
        #                 newPassword += char
        #             elif char.isnumeric():
        #                 if self.hasDigit:
        #                     print(f"skip {char}")
        #                 else:
        #                     print(f"make step {char}")
        #                     self.hasDigit = True
        #                 newPassword += char
        #             elif not char.isalnum():
        #                 if self.hasSpecial:
        #                     print(f"skip {char}")
        #                 else:
        #                     print(f"make step {char}")
        #                     self.hasSpecial = True
        #                 newPassword += char
                                
                                
        #     # decides the start direction: 
        #     # if original_password > 20:
        #     #     # start by removing
        #     #     print(password)
        #     #     self.peakCritera()
        #     #     missing = self.getFirstMissingCriteria()
        #     #     print("missing: ",  missing)
        #     #     password = password[1:]
        #     #     print("popping")
        #     #     steps +=1
            
        #     #     if self.isStrong(password) and  6 <= len(password) <= 20:
        #     #         print("STRONG, You'll be a soldier")
        #     #         print("steps: ", steps)
        #     #         # print("password: ", password.join(","))
        #     #         print("password: ", "".join(password))

        #     #         break

        #     #     if len(password) < 6: #<= len(password):
        #     #         print("too much")
        #     #         break

        #     # if original_password < 6:
        #     #     # start by adding
        #     #     # password = password + "0"
        #     #     # missing = self.getFirstMissingCriteria()
        #     #     # password += "0"
        #     #     # print("adding")
        #     #     # print(self.peakCritera())
        #     #     # print("missing: ",  missing)

        #     #     missing = self.getFirstMissingCriteria()
        #     #     password += missing
        #     #     print("adding")
        #     #     print(self.peakCritera())
        #     #     print("missing: ",  missing)
                
        #     #     # missing = self.getFirstMissingCriteria()
        #     #     # print("adding")

        #     #     # print(self.peakCritera())
        #     #     # print(f"adding [{missing}]")


        #     #     steps +=1                    
                
        #     #     if self.isStrong(password) and  6 <= len(password) <= 20:
        #     #         print("STRONG, You'll be a soldier")
        #     #         print("steps: ", steps)
        #     #         # print("password: ", password.join(","))
        #     #         print("password: ", "".join(password))
        #     #         break

        #     #     if len(password) > 20: #<= len(password):
        #     #         print("too much")
        #     #         break
        while not self.isStrong(password) or not 6 <= len(password) <= 20:
            # if original_password < 6 and len(password) >= 6 and self.isStrong(password):
            #     break
            # if original_password > 20 and len(password) <= 20 and self.isStrong(password):
            #     break
            
            if original_password > 20 and len(password) > 20:
                removed = len(password) - 20
                password = self.remove_from_repetitions(password, removed)
                steps += removed
                continue
            self.resetCritera()
            newPassword = ""
            replacements = 0
            
            for i, char in enumerate(password):
                print(char)
                if not self.checkRepeat(char, newPassword):
                    new_char = self.changeChar(char)
                    replacements += 1
                    print(f"replacement , char: {char}")
                    newPassword += new_char
                else:
                    if char.isupper():
                        if self.hasUpper:
                            print(f"skip {char}")
                        else:
                            print(f"make step {char}")
                            self.hasUpper = True
                        newPassword += char
                    elif char.islower():
                        if self.hasLower:
                            print(f"skip {char}")
                        else:
                            print(f"make step {char}")
                            self.hasLower = True
                        newPassword += char
                    elif char.isnumeric():
                        if self.hasDigit:
                            print(f"skip {char}")
                        else:
                            print(f"make step {char}")
                            self.hasDigit = True
                        newPassword += char
                    elif not char.isalnum():
                        if self.hasSpecial:
                            print(f"skip {char}")
                        else:
                            print(f"make step {char}")
                            self.hasSpecial = True
                        newPassword += char

            if original_password < 6 and len(newPassword) < 6:
                missing = self.getFirstMissingCriteria()
                newPassword += missing
                steps += 1
                print("adding missing criteria")
                print(self.peakCritera())
                print("missing: ", missing)
            else:
                steps += replacements
                        
            print("steps: ", steps)
            print("newPassword: ", newPassword)
            print("len newPassword: ", len(newPassword))
            if password == newPassword:
                break
            password = newPassword
        
        return steps


if __name__ == '__main__':

    cases = [
        # "a", #False
		# "aA1", #False 
		# "1337n!nC0d3", #True 
        # "1337n!nC0d31337n!nC0d31337n!nC0d31nnn3", #False 
        # "1337n!nC0d31337n!nC0d31337n!nC0d31337n!nC0d3133",
        # "1337n!nC0d31337n!nC0",

        "a",                                    # 1 char, missing upper, digit, special
        # "aB1",                                  # 3 chars, missing special, under 6
        # "aaa",                                  # 3 chars, all same, missing upper, digit, special
        "AAAA1",                                # 5 chars, has repetition, missing lower & special
        "abc...!!!",                              # 9 chars, all criteria met but has "..." repetition
        "aB1.aB1.aB1.aB1.aB1.",                   # 21 chars, over limit but has all criteria
        "AAAAAAAAAAAAAAAAAAAAA",                  # 21 chars, all uppercase with repetition, over limit
        "1111111111111111111111111111111111111111111111111", # 51 chars, way over but testing length
        "Aa1",                                  # 3 chars, missing special, under 6
        "aaaaaaaaaaaaaaBBBBBBBBB1!.!",         # 29 chars, long repetition patterns, over 20

    ]


# "1337n!nC0d31337n!nC0d31337n!nC0d31nnn3
# "1337n!nC" MINIMUM "...0d31337n!nC0d31337n!nC0d31nnn3"
# "1337n!nC0d31337n!nC0" MAXIMUM
# since its over it should check until it has all criteria, 
# remove all from i=20

    #> OPTION 1 (for single inputs)
    s = Solution()
    ans=[]
    for i, password in enumerate(cases):
        # print(f"___ NO.{i} ___________________________________")
        # print(f"n={i} -> {s.strongPasswordChecker(password)}\n")
        ans.append(s.strongPasswordChecker(password))

for i in ans:
    print(i)

