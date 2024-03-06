class Codec:
    def __init__(self, ):
        self.nums =  [0,1,2,3,4,5,6,7,8,9]
        self.lower_case = []




# "7 4 34"
import re
import random 
from string import punctuation, ascii_letters
import random

full_list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# random.shuffle(full_list)
randomized_full_list = ['Y', '"', 'F', '{', 'z', 'P', 'G', ')', 'Q', ',', 'K', ';', 'w', '[', 'o', '~', 'N', 'A', '^', '>', '*', '`', 'p', 'U', 'B', '}', '%', '\\', '!', 'f', '@', 'W', 'k', 'a', '/', 'R', 'y', '|', 'J', 'L', 'x', 'S', '&', 'O', 'l', 'b', '_', 'h', 'q', 'e', 't', 'u', '?', 'v', 'd', 'M', 'j', '=', 'I', ':', '#', 'V', 'i', 'T', '.', '(', 'Z', 'n', '$', 'g', ']', 'E', '-', 's', 'C', '<', 'D', 'c', 'm', 'r', 'H', '+', 'X', "'"]

code_table = dict(zip(randomized_full_list, list((range(len(randomized_full_list))))))
inverted_table = dict(zip(list((range(len(randomized_full_list)))), randomized_full_list))
# {'2': 0, '/': 1, 'G': 2, 'P': 3, 'C': 4, 'Y': 5, '9': 6, 'B': 7, '4': 8, 'o': 9, 'p': 10, 'y': 11, '%': 12, 'c': 13, 'j': 14, 'w': 15, 'z': 16, 'W': 17, 'N': 18, 'M': 19, 'O': 20, 'q': 21, '+': 22, 'l': 23, 'J': 24, 'A': 25, 'F': 26, 'u': 27, '-': 28, '7': 29, 'd': 30, 'K': 37, 'U': 32, 'k': 66, 'x': 34, 'n': 35, 'g': 36, 'L': 38, 'S': 39, 's': 40, '_': 41, 'm': 42, 'I': 43, 'D': 44, 'a': 45, 'b': 46, 'r': 47, '5': 48, '0': 49, '8': 50, 'v': 51, '3': 52, 'Q': 53, 'X': 54, '.': 55, 'i': 56, 'R': 57, '=': 58, 'f': 59, '1': 60, '&': 61, 'V': 62, 'T': 63, '6': 64, 'e': 65, 'Z': 67, 'H': 68, 'E': 69, 't': 70, 'h': 71}
characters = punctuation+ascii_letters #no digits
#['p', 'l', 'e', 'a', 's', 'e', ',', ' ', 'd', 'o', 'n', "'", 't', ' ', 'd', 'e', 'c', 'o', 'd', 'e', ' ', 'm', 'e', ' ', ':', '('] [*input_str]

def encode(input_str):
    encoded_str=""
    for i in [*input_str]:
        x = "" #the encoded value of i
        s = "" #stands for seperator
        if i ==" ":
            x = random.choice(characters)
            s = random.choice(characters)
        else:
            x = str(code_table[str(i)])
            s = random.choice(characters)
            x = str(x)
        encoded_str+=x+s
    return encoded_str
        
def decode(encoded_str):
    encode_str_w_spaces = ""
    for i, x in enumerate(encoded_str):
        if i+1!=len(encoded_str):
            if not encoded_str[i+1].isdigit() and not x.isdigit():
                encode_str_w_spaces+=" "
            encode_str_w_spaces+=x
        else: 
            encode_str_w_spaces+=x
    pattern = r' [a-zA-Z\s\W] '
    encode_str_w_spaces =re.split(pattern, encode_str_w_spaces)# " ".join(re.split(pattern, encode_str_w_spaces))
    pattern = r'[^0-9]+'
    res_list=[]
    for i in encode_str_w_spaces:
        r = list(filter(None, re.split(pattern, i)))
        r = "".join([inverted_table[int(i)] for i in r])
        res_list.append(r)
    return " ".join(res_list)    

def compress(string):

    res = ""

    count = 1

    #Add in first character
    res += string[0]

    #Iterate through loop, skipping last one
    for i in range(len(string)-1):
        if(string[i] == string[i+1]):
            count+=1
        else:
            if(count > 1):
                #Ignore if no repeats
                res += str(count)
            res += string[i+1]
            count = 1
    #print last one
    if(count > 1):
        res += str(count)
    return res
    
input_str = "please, don't decode me :("  
encoded_str = encode(input_str)

# print(decode(encoded_str))

str_="Please, don't encode me :("
str_ = encoded_str.encode(encoding='ascii')
# str_=" 01010000 01101100 01100101 01100001 01110011 01100101"
compressed_str = compress(str(str_))
print(compressed_str)

counter=0
limit=4

"code"
co = 20
de = 377
len_ = 73
x=len_
if de > len_:
    x=de
elif co>len_:
    x=co
    while x > len_:
        x-=len_
new_co=mydict[co]
new_de=mydict[de]
counter+=1
# ==> "r", "#"
if len(full_str) > limit:
    repeat...
else:
    
    '''  e8dH  +  04  '''
    return "".join(new_str_list)+counter.mate_double_digit()

    
str_= [20,377]