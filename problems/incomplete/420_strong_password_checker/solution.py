# import random

# class Solution:
#     def __init__(self, ):
#         # Criteria
#         self.length_limit = False 
#         self.has_lower = False
#         self.has_upper = False
#         self.has_digit = False
#         self.no_repetition = False
        
#         # self.password_state:str = ""
#         # self.password_template = "qso3Km" #Oh, now we're cheating!
#         self.input_password = ""
#         self.password = ""
#         length_appropriate_password = ""
#         self.output_password = ""

#         # Final verdict
#         self.is_strong = False
#         self.steps = 0 #number of steps to make self.password into strong_password
    
#     @property
#     def criteria(self,) -> list[bool]:
#         return [
#             self.length_limit,
#             self.has_lower,
#             self.has_upper,
#             self.has_digit,
#             self.no_repetition,
#             ]
#     # False, True, True, True, False]
    
#     def gen_random_character(self, last_letter_in_password):
#         #NOTE: amount: number of characters from the self.password input
#         #NOTE: k: a random choice from a range between amount of character in self.password input and (max length limit - len(self.password input))
#         # n=random.choice(range((6-self.len_input_password), (20-self.len_input_password)))
#         digit = '0123456789'
#         upper = 'abcdefghijklmnopqrstuvwxyz'
#         lower = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#         first_extention_letter = ''.join(random.choices((digit+upper+lower).replace(last_letter_in_password,"")))  
#         extention_str = first_extention_letter + ''.join(random.choices((digit+upper+lower), k=(6-(1+len(self.password)))))
#         return self.thorough_checkup(extention_str, digit, upper, lower)

#     def thorough_checkup(self, extention_str, digit, upper, lower):
#         char_update = "" 

#         print("Printing from thorough_checkup:")
#         print(f'[0] char_update: "{char_update}"')
#         print(f'[0] extention_str: "{extention_str}"')
        
#         if not self.check_lower(extention_str):#():
#             new_char, extention_str  = self.replace_one_char(extention_str, lower)
#             char_update+=new_char
#             print(f'[1] char_update: "{char_update}"')
#             print(f'[1] extention_str: "{extention_str}"')
        
#         if not self.check_upper(extention_str):
#             new_char, extention_str  = self.replace_one_char(extention_str, upper)
#             char_update+=new_char
#             print(f'[2] char_update: "{char_update}"')
#             print(f'[2] extention_str: "{extention_str}"')

#         if not self.check_digit(extention_str):
#             new_char, extention_str  = self.replace_one_char(extention_str, digit)
#             char_update+=new_char
#             print(f'[3] char_update: "{char_update}"')
#             print(f'[3] extention_str: "{extention_str}"')

#         if self.no_repetition:
#             new_char, extention_str = self.replace_dups(extention_str, 1, (digit+upper+lower))
#             char_update+=new_char
#             print(f'[4] char_update: "{char_update}"')
#             print(f'[4] extention_str: "{extention_str}"')
#         return char_update+extention_str

#     # def replace_dups(self, password, i, char_group):
#     #     return random.choice(char_group), password.replace((password[i+1]), "")
#     #     # for i, char in enumerate(self.password):
#         #     if char != [self.password[i+1], self.password[i+2]]:
#         #         # print(extention_str.replace((extention_str[i+1]), random.choice(char_group)))
#         #         return  random.choice(char_group), extention_str.replace((extention_str[i+1]), "")

#     def replace_dups(self, *args) -> str or [str,str]:
#         self.no_repetition = False
#         password = dict(enumerate(self.password))
#         if args:
#             password = dict(enumerate(args))
#         chars = ""
#         password_res = password
#         for i, char in password.items():
#             if i+2 >= len(password):
#                 break
#             # if [char, char] == [password[i+1], password[i+2]]:
#             if char == password[i+1] and password[i+2]:
#                 newchar = random.choice('0123456789'+'abcdefghijklmnopqrstuvwxyz'+'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#                 chars += newchar
#                 if args:
#                     password_res[i+1]=""
#                 else:
#                     password_res[i+1]=newchar
#                 i = i+2

#         password_res = "".join(password_res.values())
#         self.no_repetition = True
#         if args:
#             return chars, password_res
#         return password_res
    
#     def replace_one_char(self, extention_str, char_group):
        
#         print(f'replace_one_char() was triggered, input:, extention_str="{extention_str}", char_group="{char_group}"')
#         return random.choice(char_group), extention_str.replace((extention_str)[0], "")

#     def strongPasswordChecker(self, password: str)-> int:
#         self.password = password
#         self.output_password = password
#         self.input_password = password

#         print("\n","-"*50)
#         print("variables before check_length():")
#         print(f"self.input_password: {self.input_password}, len:{len(self.input_password)}")
#         print(f"length_appropriate_password: "", len:0")
#         print(f"self.steps: 0")
#         print("-"*50)

#         if not self.check_length():
#             self.password = self.change_length()
#             self.steps = abs(len(self.password)-(len(self.input_password)))

#         print("\n","-"*50)
#         print("variables After check_length():")
#         print(f"self.input_password: {self.input_password}, len:{len(self.input_password)}")
#         print(f"length_appropriate_password: {self.password }, len:{len(self.password )}")
#         print(f"self.steps: {self.steps}")
#         print("-"*50)

#         # if not self.check_length(self.len_input_password, "short"):
#         #     print("PASSWORD = TOO SHORT")
#         #     #too short
#         #     length_appropriate_password = self.password + self.gen_random_character(self.password[-1])
        
#         # elif not self.check_length(self.len_input_password, "long"):
#         #     print("PASSWORD = TOO LONG")
#         #     # too long
#         #     length_appropriate_password = self.password[:20]
#         #     print(f"unedited shortened password: {length_appropriate_password}")
#         # add difference to counter
#         # self.steps = abs(len(length_appropriate_password)-(len(self.password)))

#         # for i in length_appropriate_password:
#         if not self.no_repetition:
#             self.password  = self.replace_dups()
#             # self.steps = abs(len(self.password )-(len(self.input_password)))
#             self.steps = self.get_difference(self.password, self.input_password)
#         print("DUPLICAT FIXED PASSWORD: ", self.password )
#         print("___________________________________________________")

#         # length_appropriate_password = self.check_criteria(length_appropriate_password)

#         print("\n FINAL CHECK BEFORE OUTPUT: \n self.check_criteria(): ", self.check_criteria(),"\n")
#         # print("self.check_criteria: ", self.check_criteria(duplicate_checked_password),"\n")

#         if self.check_criteria(): #checks if any criteria was false
#             print("if self.check_criteria(duplicate_checked_password) == TRUE:  was triggered")
#             print(self.criteria)
#             # print(self.check_criteria(), " sould be TRUE")
#             print("Returning final output:")
#             print("="*50)
#             # print(True, self.check_criteria(length_appropriate_password))
#             # print(length_appropriate_password)
#             self.output_password = self.password
            
#             return self.steps
#         # elif self.check_repetition(duplicate_checked_password):
#         #     new_char, extention_str = self.replace_dups(extention_str, ('0123456789'+'abcdefghijklmnopqrstuvwxyz'+'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
#         #     self.strongPasswordChecker(duplicate_checked_password)
#         else:
#             print("if self.check_criteria(duplicate_checked_password) == FALSE:  was triggered")
#             print(self.criteria)
#             # print(self.check_criteria(), " sould be FALSE")
#             # print("rerunning strongPasswordChecker():")
#             # print("_"*50)
#             # self.strongPasswordChecker(self.password)

#     def set_steps(self, ):
#         self.steps = abs(len(self.password)-(len(self.input_password)))


#     def check_criteria(self) -> bool:
#         self.check_length(), self.check_lower(), self.check_upper(), self.check_digit(),
#         return all([
#         self.length_limit, 
#         self.has_lower,
#         self.has_upper,
#         self.has_digit,
#         self.no_repetition,
#             ])
#     # def check_publicates(self)-> bool:
#     #     self.length_limit = 6 >= len(self.password) >= 20
#     #     return self.length_limit
    
#     def check_length(self, )->bool:
#         self.length_limit = 6 <= len(self.password) <= 20
#         return self.length_limit
    
#     def change_length(self, )-> str:
#         if 6 > len(self.password):
#             print(f"check_length -> PASSWORD = TOO SHORT :  {self.password}:{len(self.password)}")
#             self.length_limit = True
#             print("*******************************")
#             print(self.gen_random_character(self.password[-1]))
#             print(self.password)
#             return self.password + self.gen_random_character(self.password[-1])
#         elif len(self.password) > 20:
#             print(f"check_length -> PASSWORD = TOO LONG :  {self.password}:{len(self.password)}")
#             self.length_limit = True
#             return self.password[:20]
#         else:
#             return self.password
    
#     def check_lower(self, *args)->bool:
#         self.has_lower = any(x.islower() for x in (args if args else self.password))
#         return self.has_lower

#     def check_upper(self, *args)->bool:
#         self.has_upper = any(x.isupper() for x in (args if args else self.password))
#         return self.has_upper
        
#     def check_digit(self, *args)->bool:
#         self.has_digit = any(x.isdigit() for x in (args if args else self.password))
#         return self.has_digit

#     def get_difference(self, old, new)->list:
        
#         print(old)
#         print(new)
        
#         count=0
#         # x = len(new)-len(old)
#         # print(f"{x} = {len(new)}{len(old)}")
#         # if x < 0:
#         #     count += -x
#         #     print(f"{count}+= {-x} ")
#         # else:
#         #     count += x
#         #     print(count)
        
#         # for i, y in zip(new, old):
#         #     if i != y:
#         #         count += 1
        
#         # print("XXXXXXXXXXXXXXXXXX")
#         # print(count)
#         # print("x"*25)
#         return count






#     # TEMP WHILE TESTING
#     # def check_length(self, len_input_password:str, *args)->bool:
#     #     if args == "short":
#     #         return 6 <= len_input_password
        
#     #     if args == "long":
#     #         return len_input_password <= 20 
#     #     else:
#     #         return 6 <= len_input_password <= 20 
    
import random

class Solution:
    def __init__(self, ):
        # Criteria
        self.length_limit = False 
        self.has_lower = False
        self.has_upper = False
        self.has_digit = False
        self.no_repetition = False
        
        # self.password_state:str = ""
        # self.password_template = "qso3Km" #Oh, now we're cheating!
        self.input_password = ""
        self.password = ""
        length_appropriate_password = ""
        self.output_password = ""

        # Final verdict
        self.is_strong = False
        self.steps = 0 #number of steps to make self.password into strong_password
    
    @property
    def criteria(self,) -> list[bool]:
        return [
            self.length_limit,
            self.has_lower,
            self.has_upper,
            self.has_digit,
            self.no_repetition,
            ]
    # False, True, True, True, False]
    
    def gen_random_character(self, last_letter_in_password):
        #NOTE: amount: number of characters from the self.password input
        #NOTE: k: a random choice from a range between amount of character in self.password input and (max length limit - len(self.password input))
        # n=random.choice(range((6-self.len_input_password), (20-self.len_input_password)))
        digit = '0123456789'
        upper = 'abcdefghijklmnopqrstuvwxyz'
        lower = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        first_extention_letter = ''.join(random.choices((digit+upper+lower).replace(last_letter_in_password,"")))  
        extention_str = first_extention_letter + ''.join(random.choices((digit+upper+lower), k=(6-(1+len(self.password)))))
        return self.thorough_checkup(extention_str, digit, upper, lower)

    def thorough_checkup(self, extention_str, digit, upper, lower):
        char_update = "" 

        print("Printing from thorough_checkup:")
        print(f'[0] char_update: "{char_update}"')
        print(f'[0] extention_str: "{extention_str}"')
        
        if not self.check_lower(extention_str):#():
            new_char, extention_str  = self.replace_one_char(extention_str, lower)
            char_update+=new_char
            print(f'[1] char_update: "{char_update}"')
            print(f'[1] extention_str: "{extention_str}"')
        
        if not self.check_upper(extention_str):
            new_char, extention_str  = self.replace_one_char(extention_str, upper)
            char_update+=new_char
            print(f'[2] char_update: "{char_update}"')
            print(f'[2] extention_str: "{extention_str}"')

        if not self.check_digit(extention_str):
            new_char, extention_str  = self.replace_one_char(extention_str, digit)
            char_update+=new_char
            print(f'[3] char_update: "{char_update}"')
            print(f'[3] extention_str: "{extention_str}"')

        if self.no_repetition:
            new_char, extention_str = self.replace_dups(extention_str, 1, (digit+upper+lower))
            char_update+=new_char
            print(f'[4] char_update: "{char_update}"')
            print(f'[4] extention_str: "{extention_str}"')
        return char_update+extention_str 

    # def replace_dups(self, password, i, char_group):
    #     return random.choice(char_group), password.replace((password[i+1]), "")
    #     # for i, char in enumerate(self.password):
        #     if char != [self.password[i+1], self.password[i+2]]:
        #         # print(extention_str.replace((extention_str[i+1]), random.choice(char_group)))
        #         return  random.choice(char_group), extention_str.replace((extention_str[i+1]), "")
    def replace_dups(self, *args) -> str or [str,str]:
        self.no_repetition = False
        password = dict(enumerate(self.password))
        if args:
            password = dict(enumerate(args))
        chars = ""
        password_res = password
        for i, char in password.items():
            if i+2 >= len(password):
                break
            if [char, char] == [password[i+1], password[i+2]]:
                newchar = random.choice('0123456789'+'abcdefghijklmnopqrstuvwxyz'+'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                chars += newchar
                if args:
                    password_res[i+1]=""
                else:
                    password_res[i+1]=newchar

        password_res = "".join(password_res.values())
        self.no_repetition = True
        if args:
            return chars, password_res
        return password_res
    # def replace_dups(self, **args) -> str:
    #     print("______________________CHECKING REPITITION______________________")
    #     self.no_repetition = False
    #     password = self.password
    #     if args:
    #         password = args
    #     iterating_password = password
            
    #     # if self.length_limit:
    #         # print(f"    length_limit=True")
    #     newchars=""
    #     for i, char in enumerate(password):
    #         try:
    #             # print(f"{[char, char]} != {password[i+1]}, {password[i+2]} ==> {[char, char] != [password[i+1], password[i+2]]}")
    #             # char, char != [password[i+1], password[i+2]]
    #             # j != j, j ==> True
    #             if i >= len(password[i+2]):
    #                 break
    #             else:

                
    #                 if [char, char] != [password[i+1], password[i+2]]:
    #                     print(f"        {[char, char]} != {password[i+1]}, {password[i+2]} ==> {[char, char] != [password[i+1], password[i+2]]}")
    #                     newchar, password = random.choice('0123456789'+'abcdefghijklmnopqrstuvwxyz'+'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), password.replace((password[i+1]), "")
    #                     newchars += newchar
    #                     # self.set_steps()
    #                     # self.no_repetition = True
    #         except:
    #             print("all Done")
    #         if args:
    #             return newchars, password
    #         return newchars+password
    #     self.no_repetition = True
    #         # try: 
    #             # if char != [password[i+1], password[i+2]]:
    #             #     print(f"        duplicate = True (bad)")
    #             #     newchar, newpassword = random.choice('0123456789'+'abcdefghijklmnopqrstuvwxyz'+'ABCDEFGHIJKLMNOPQRSTUVWXYZ'), password.replace((password[i+1]), "")
    #             #     self.set_steps()
    #             #     self.no_repetition = True
    #             #     if args:
    #             #         return newchar, newpassword
    #             #     return newchar+newpassword

    #         #     else:
    #         #         print(f"        duplicate = False (good)")
    #         #         # print(f"    length")
    #         #         self.no_repetition = True
    #         #         return password
                
    #         # except IndexError:
    #         #         self.no_repetition = True
    #         #         return password
    #     # else:
    #     #     print(f"    length_limit=False")

    #!  ERROR OCCOURED HERE 
    # Når passordet er for langt, kødder denne seg.
    def replace_one_char(self, extention_str, char_group):
        
        print(f'replace_one_char() was triggered, input:, extention_str="{extention_str}", char_group="{char_group}"')
        return random.choice(char_group), extention_str.replace((extention_str)[0], "")

    def strongPasswordChecker(self, password: str)-> int:
        self.password = password
        self.output_password = password
        self.input_password = password

        print("\n","-"*50)
        print("variables before check_length():")
        print(f"self.input_password: {self.input_password}, len:{len(self.input_password)}")
        print(f"length_appropriate_password: "", len:0")
        print(f"self.steps: 0")
        print("-"*50)

        if not self.check_length():
            self.password = self.change_length()
        self.steps = abs(len(self.password)-(len(self.input_password)))

        print("\n","-"*50)
        print("variables After check_length():")
        print(f"self.input_password: {self.input_password}, len:{len(self.input_password)}")
        print(f"length_appropriate_password: {self.password }, len:{len(self.password )}")
        print(f"self.steps: {self.steps}")
        print("-"*50)

        # if not self.check_length(self.len_input_password, "short"):
        #     print("PASSWORD = TOO SHORT")
        #     #too short
        #     length_appropriate_password = self.password + self.gen_random_character(self.password[-1])
        
        # elif not self.check_length(self.len_input_password, "long"):
        #     print("PASSWORD = TOO LONG")
        #     # too long
        #     length_appropriate_password = self.password[:20]
        #     print(f"unedited shortened password: {length_appropriate_password}")
        # add difference to counter
        # self.steps = abs(len(length_appropriate_password)-(len(self.password)))

        # for i in length_appropriate_password:
        if not self.no_repetition:
            self.password  = self.replace_dups()
        self.steps = abs(len(self.password )-(len(self.input_password)))
        print("DUPLICAT FIXED PASSWORD: ", self.password )
        print("___________________________________________________")

        # length_appropriate_password = self.check_criteria(length_appropriate_password)

        print("\n FINAL CHECK BEFORE OUTPUT: \n self.check_criteria(): ", self.check_criteria(),"\n")
        # print("self.check_criteria: ", self.check_criteria(duplicate_checked_password),"\n")

        if self.check_criteria(): #checks if any criteria was false
            print("if self.check_criteria(duplicate_checked_password) == TRUE:  was triggered")
            print(self.criteria)
            # print(self.check_criteria(), " sould be TRUE")
            print("Returning final output:")
            print("="*50)
            # print(True, self.check_criteria(length_appropriate_password))
            # print(length_appropriate_password)
            self.output_password = self.password
            
            return self.steps
        # elif self.check_repetition(duplicate_checked_password):
        #     new_char, extention_str = self.replace_dups(extention_str, ('0123456789'+'abcdefghijklmnopqrstuvwxyz'+'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        #     self.strongPasswordChecker(duplicate_checked_password)
        else:
            print("if self.check_criteria(duplicate_checked_password) == FALSE:  was triggered")
            print(self.criteria)
            # print(self.check_criteria(), " sould be FALSE")
            # print("rerunning strongPasswordChecker():")
            # print("_"*50)
            # self.strongPasswordChecker(self.password)

    def set_steps(self, ):
        self.steps = abs(len(self.password)-(len(self.input_password)))


    def check_criteria(self) -> bool:
        self.check_length(), self.check_lower(), self.check_upper(), self.check_digit(),
        return all([
        self.length_limit, 
        self.has_lower,
        self.has_upper,
        self.has_digit,
        self.no_repetition,
            ])
    # def check_publicates(self)-> bool:
    #     self.length_limit = 6 >= len(self.password) >= 20
    #     return self.length_limit
    
    def check_length(self, )->bool:
        self.length_limit = 6 <= len(self.password) <= 20
        return self.length_limit
    
    def change_length(self, )-> str:
        if 6 > len(self.password):
            print(f"check_length -> PASSWORD = TOO SHORT :  {self.password}:{len(self.password)}")
            self.length_limit = True
            return self.password + self.gen_random_character(self.password[-1])
        elif len(self.password) > 20:
            print(f"check_length -> PASSWORD = TOO LONG :  {self.password}:{len(self.password)}")
            self.length_limit = True
            return self.password[:20]
        else:
            return self.password
    
    def check_lower(self, *args)->bool:
        self.has_lower = any(x.islower() for x in (args if args else self.password))
        return self.has_lower

    def check_upper(self, *args)->bool:
        self.has_upper = any(x.isupper() for x in (args if args else self.password))
        return self.has_upper
        
    def check_digit(self, *args)->bool:
        self.has_digit = any(x.isdigit() for x in (args if args else self.password))
        return self.has_digit






    # TEMP WHILE TESTING
    # def check_length(self, len_input_password:str, *args)->bool:
    #     if args == "short":
    #         return 6 <= len_input_password
        
    #     if args == "long":
    #         return len_input_password <= 20 
    #     else:
    #         return 6 <= len_input_password <= 20 
    
    