'''
class Solution:
    def romanToInt(self, s: str) -> int:
        pass

def main():
    inputs = [-121, 121, 10 , 1881]
    s = Solution()
    for x in inputs:
        result = s.isPalindrome(x)
        print(result)

if __name__ == '__main__':
    main()
'''


values = {
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        }

special = {

        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
}



# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.

# s = "III"
# for index, i in enumerate(s):
#     if s[index]

# if 'I' 



def switch_dict(s):
    result = [values.get(i) for i in s]
    print(result)
    return sum(result)


s = "MCMXCIV"
keys = [i for i in values.keys()]
for index, i in enumerate(keys):
    if i in s[:]: 
        print(i)




# string = s.split(i)
# print(string)
# str_list = s.split(keys)
# print(str_list)
# res = s.get(values)
# print(res)


# res = switch_dict(s)
# print(res)


# romans = ["III", "LVIII", "MCMXCIV"]
# for s in romans:
#     res = switch_dict(s)
#     print(res)