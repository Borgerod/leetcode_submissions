import random

class Solution:
    def __init__(self, ):
        # Criteria
        self.length_limit = False 
        self.has_lower = False
        self.has_upper = False
        self.has_digit = False
        self.no_repetition = False
        
        self.password_state:str = ""
        self.password_template = "qso3Km" #Oh, now we're cheating!

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
    
    def gen_random_character(self, last_letter_in_password):
        #NOTE: amount: number of characters from the self.password input
        #NOTE: k: a random choice from a range between amount of character in self.password input and (max length limit - len(self.password input))
        # n=random.choice(range((6-self.len_input_password), (20-self.len_input_password)))
        digit = '0123456789'
        upper = 'abcdefghijklmnopqrstuvwxyz'
        lower = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        first_extention_letter = ''.join(random.choices((digit+upper+lower).replace(last_letter_in_password,"")))  
        extention_str = first_extention_letter + ''.join(random.choices((digit+upper+lower), k=(6-(1+self.len_input_password))))
        return self.thorough_checkup(extention_str, digit, upper, lower)

    def thorough_checkup(self, extention_str, digit, upper, lower):
        char_update = "" 
        if not self.check_lower(self.password)(extention_str):
            new_char, extention_str  = self.replace_one_char(extention_str, lower)
            char_update+=new_char
        
        if not self.check_upper(self.password)(extention_str):
            new_char, extention_str  = self.replace_one_char(extention_str, upper)
            char_update+=new_char
        
        if not self.check_digit(self.password)(extention_str):
            new_char, extention_str  = self.replace_one_char(extention_str, digit)
            char_update+=new_char
        
        if self.check_repetition(extention_str):
            new_char, extention_str = self.replace_dups(extention_str, (digit+upper+lower))
            char_update+=new_char

        return char_update+extention_str 

    def replace_dups(self, extention_str, char_group):
        for i, char in enumerate(self.password):
            if char == [self.password[i+1], self.password[i+2]]:
                # print(extention_str.replace((extention_str[i+1]), random.choice(char_group)))
                return  random.choice(char_group), extention_str.replace((extention_str[i+1]), "")
    
    def replace_one_char(self, extention_str, char_group):
        return random.choice(char_group), extention_str.replace((extention_str)[0], "")

    def strongPasswordChecker(self, password: str)-> int:
        self.password = password
        # first we check the limit so we know how much we ned to change
        self.len_input_password = len(self.password) #aka "amount"
        length_appropriate_password = self.password #default assumes length is correct 
        if not self.check_length(self.len_input_password, "short"):
            #too short
            length_appropriate_password = self.password + self.gen_random_character(self.password[-1])
        elif not self.check_length(self.len_input_password, "long"):
            # too long
            length_appropriate_password = self.password[:20]
        # add difference to counter
        self.steps = abs(len(length_appropriate_password)-(len(self.password)))
        
        
        # for i in length_appropriate_password:
        if self.check_criteria(length_appropriate_password): #checks if any criteria was false
            # print(True, self.check_criteria(length_appropriate_password))
            # print(length_appropriate_password)
            return self.steps
        elif self.check_repetition(length_appropriate_password):
            new_char, extention_str = self.replace_dups(extention_str, ('0123456789'+'abcdefghijklmnopqrstuvwxyz'+'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
            self.strongPasswordChecker(length_appropriate_password)
        else:
            self.strongPasswordChecker(length_appropriate_password)
    
                

    # def optimize_password(self, self.password):
    #     criteria_names = ['length_limit','has_lower','has_upper','has_digit','no_repetition']
    #     self.steps = len([self.name for self.prop, self.name in zip(self.criteria, criteria_names) if not self.prop])
    #     print([self.name for self.prop, self.name in zip(self.criteria, criteria_names) if not self.prop])
    #     # # failed_criteria = [i for i in self.criteria if not i]
    #     # for prop in [name for self.prop, name in zip(self.criteria, criteria_names) if not self.prop]:
    #     #     print(self.prop)

    def check_criteria(self) -> bool:
        return any([
            self.check_length(len(self.password)),
            self.check_lower(self.password)(self.password),
            self.check_upper(self.password)(self.password),
            self.check_digit(self.password)(self.password),
            self.check_repetition(self.password),
            ])
          
    # def check_criteria(self, self.password) -> list[bool]:
    #     self.length_limit = self.check_length(self.password)
    #     self.has_lower = self.check_lower(self.password)(self.password)
    #     self.has_upper = self.check_upper(self.password)(self.password)
    #     self.has_digit = self.check_digit(self.password)(self.password)
    #     self.no_repetition = self.check_repetition(self.password)
      
    def check_repetition(self, self.password:str) -> bool:
        if self.length_limit:
            for i, char in enumerate(self.password):
                if char != [self.password[i+1], self.password[i+2]]:
                    return True
        
    def check_length(self, len_input_password:str, *args)->bool:
        if args == "short":
            return 6 <= len_input_password
        
        if args == "long":
            return len_input_password <= 20 
        else:
            return 6 <= len_input_password <= 20 

    def check_lower(self, self.password:str)->bool:
        x = lambda self.password: any(x.islower() for x in self.password)
        return lambda self.password: any(x.islower() for x in self.password) # must have at least one uppercase

    def check_upper(self, self.password:str)->bool:
        return lambda self.password: any(x.isupper() for x in self.password) # must have at least one lowercase

    def check_digit(self, self.password:str)->bool:
        return lambda self.password: any(x.isdigit() for x in self.password) # must have at least one uppercase


if __name__ == '__main__':
    self.password = "Password123"
    self.password = "a"
    s = Solution()
    res = s.strongPasswordChecker(self.password)
    # print(res)
