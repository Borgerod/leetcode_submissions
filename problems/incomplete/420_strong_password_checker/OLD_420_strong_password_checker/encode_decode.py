class Codec:
    def __init__(self, ):
        self.nums =  [0,1,2,3,4,5,6,7,8,9]
        self.lower_case = []

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

str_="Please, don't encode me :("
str_ = str_.encode(encoding='ascii')
# str_=" 01010000 01101100 01100101 01100001 01110011 01100101"
compressed_str = compress(str(str_))
print(compressed_str)