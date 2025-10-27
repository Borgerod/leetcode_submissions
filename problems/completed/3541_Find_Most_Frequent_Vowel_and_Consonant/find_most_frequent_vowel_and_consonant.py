class Solution:
    '''
    tags: Hash Table, String, Counting
    '''

    def maxFreqSum(self, s: str) -> int:
        
        '''
        1.0) quickest solution, sort and count into dict, then set leading vowel and consonant, return leader picks.
             NOTE: I assume there's a built in way of doing this but I don't want to use it. 
        '''
        vowels = ['a', 'e', 'i', 'o', 'u']
        freqs = {}
        for char in s:
            if char in freqs: 
                freqs[char] += 1
            else: 
                freqs[char] = 1
            
        top = 0
        have_vowel = False
        have_cons = False

        # Sort items on the fly, no dict creation
        for char, val in sorted(freqs.items(), key=lambda x: x[1], reverse=True):
            if have_cons and have_vowel:
                break
            if not have_cons and char not in vowels:
                top += val
                have_cons = True
            elif not have_vowel and char in vowels:
                top += val
                have_vowel = True
        return top


    def maxFreqSum(self, s: str) -> int:
        
        '''
        1.1) AI asisted to optimize some parts. 
        '''
        vowels = {'a', 'e', 'i', 'o', 'u'}
        freqs = {}
        max_vowel = 0
        max_cons = 0

        for char in s:
            freqs[char] = freqs.get(char, 0) + 1
            
        # Find top vowel and top consonant
        for char, val in freqs.items():
            if char in vowels:
                if val > max_vowel:
                    max_vowel = val
            else:
                if val > max_cons:
                    max_cons = val
        return max_vowel + max_cons


if __name__ == '__main__':

    cases = [
        "bx",
        "successes",
        "aeiaeia",
        "dlqljueerdujafsodzxlgexgyhhtllwbcimdgcptfjzdhkkpdaaxezbhehndcggmncbhrckmouzxwapowplcmnjuwxxbgadawvan",
        "dpnmoikbibfceudlaqdoxejewxxbqgkhcruhpwgvqppdpyrwgfcybmghemdeihlxmuqgtjcgtpesmapxygztmiblpbvresghndjm",
        "ohjkzgmoxbaeamfqlllduiksohawcjoxfntxvmjgvzxbgmctnvhyjkrnqmjdtbrpqbsavvubhakkkibzlqaerwjffstebwmvxnbt",
        "ohxeuyizpdrzuyxzooqsztkaxysccnozptmwehnpxrimjbncnjbugjjnwdhbbosyswnnrcutezurgzaijuoydijfyjctbcrxrcjo",
        "aywmilyayohvtozpljdmijlvobegngaznfmtzutpvlrjlljrthwxvfegvaxmaxqsjyludsgbjzdlbjmchsjfpckpybozwxwmgzxl",
    ]

    #> OPTION 1 (for single inputs)
    solution = Solution()
    for i, s in enumerate(cases):
        print(f"___ NO.{i} ___________________________________")
        print(f"n={i} -> {solution.maxFreqSum(s)}\n")

'''
import random

def random_string(length):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=length))

cases = [
    random_string(100),
    random_string(100),
    random_string(100),
    random_string(100),
    random_string(100),
    random_string(100),
    random_string(100),
    random_string(100),
    random_string(100),
    random_string(100),
    random_string(100),
    random_string(100),
]

for case in cases:
    print(case)
'''
