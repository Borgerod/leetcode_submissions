# # import random 

# # class URLShortener:
# #     def __init__(self):
# #         self.characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# #         self.base = len(self.characters)

# #     def encode(self, num):
# #     # def encode(self, ):
# #         # num = random.randint(100µ000,1000000)
# #         short_url = ""
# #         while num > 0:
# #             remainder = num % self.base #Hva som er igjen etter man dividerer og runder av. eks: 10/3 = 3.333 ~> 9/3 = 3(1) 1 is remainding
# #             short_url = self.characters[remainder] + short_url #remainder brukes til å finne en random character fra base listen. 
# #             num = num // self.base #Så deler man det randome nummeret med lengden på base (character listen)
# #             #dette gjør man helt frem til num = 0
# #         return "http://tinyurl.com/" + short_url

# #     def decode(self, short_url):
# #         print("___ DECODEING ___")
# #         short_url = short_url.split("/")[-1] #vi splitter url'en siden det bare er koden etter "tinyurl.com/" vi er intressert i
# #         num = 0
# #         for char in short_url: #itererer igjennom koden. 
# #             ''' self.characters.index(char): indexen til bokstaven i koden. eksempel i "2dWn" er char (2): index nr 2 i characters. '''
# #             print(f" char: {char}")
# #             print(f" num before: {num}")
# #             num = num * self.base + self.characters.index(char) #
# #             print(f"self.characters.index(char): {self.characters.index(char)}")
# #             print(f" self.base: {self.base}")
# #             print(f" = num after: {num}")
# #             print("_"*20)
# #         print("FINAL: ",num)
# #         print("_"*50)
# #         print()
# #         return f"Original URL: http://{num}"
    

# # print("_"*50)
# # # Example usage
# # shortener = URLShortener()

# # long_url = "https://www.example.com/some/long/url"
# # short_url = shortener.encode(123456)  # You can use an auto-incremented integer as the unique identifier
# # # short_url = shortener.encode()  # You can use an auto-incremented integer as the unique identifier

# # # print(f"Original URL: {long_url}")
# # # print(f"Short URL: {short_url}")

# # decoded_url = shortener.decode(short_url)
# # print(decoded_url)


# class URLShortener:
#     def __init__(self):
#         self.characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/=&%!?_:-."
#         self.base = len(self.characters)

#     def encode(self, num):
#         short_url = ""
#         print("num in encode: ", num)
#         while num > 0:
#             remainder = num % self.base
#             short_url = self.characters[remainder] + short_url
#             num = num // self.base
#         return "http://tinyurl.com/" + short_url

#     def decode(self, short_url):
#         short_url = short_url.split(".com/")[-1]
#         num = 0
#         print(short_url)
#         for char in short_url:
#             num = num * self.base + self.characters.index(char)
#         num_str = str(num)
#         split_list = [int(num_str[i:i+2]) for i in range(0, len(num_str), 2)]
#         return  "https://www."+"".join([self.characters[i] for i in split_list])

#     def divider(self, num):
#         ''' will devide indentification number url until it has a certain length, then add the amount of divitions to the end of the number.'''
#         len_num = len(str(num))
#         # while len_num > 6:



#     def find_original_characters(self, num):
#         original_characters = ""
#         while num > 0:
#             remainder = num % self.base
#             original_characters = self.characters[remainder] + original_characters
#             num = num // self.base
#         return original_characters

#     def make_identifier_num_from_url(self, long_url):
#         long_url = long_url.split("//www.")[-1]
#         print(long_url)
#         num = int(''.join([f"{self.characters.index(char):02}" for char in long_url]))
#         return self.divider(num)
            
        


# # Example usage
# shortener = URLShortener()

# # long_url = "http://www.example.com/some/long/url"
# long_url = "http://www.link.com"
# print(f"Original URL: {long_url}")
# num = shortener.make_identifier_num_from_url(long_url)
# short_url = shortener.encode(num)  # You can use an auto-incremented integer as the unique identifier
# # short_url = shortener.encode(123456)  # You can use an auto-incremented integer as the unique identifier

# print(f"Short URL: {short_url}")

# decoded_url = shortener.decode(short_url)
# print("Decoded url: ", decoded_url)



# µprint(3o456x66v11)
# 3.456*66**11
# Example usage






# def compress_to_shortest_notation(number):
#     if number == 0:
#         return "0"

#     exponent = 0
#     while abs(number) >= 1000:
#         number /= 1000
#         exponent += 1

#     mantissa_str = f"{number:.3f}".rstrip('0').rstrip('.')
#     exponent_str = f"*1000**{exponent}" if exponent != 0 else ""

#     compressed_notation = mantissa_str + exponent_str

#     return compressed_notation

# # Example usage
# number = 1234567890.12345  # Example number
# compressed_notation = compress_to_shortest_notation(number)
# print(compressed_notation)
# print(1.235*1000**3)



# def compress_to_custom_notation(number):
#     if number == 0:
#         return "0"

#     notation = ""

#     # Handle negative numbers
#     if number < 0:
#         notation += "-"
#         number = abs(number)

#     while number >= 2:
#         root = 2
#         while number % root != 0:
#             root += 1
#         power = 0

#         while number % (root ** (power + 1)) == 0:
#             power += 1

#         notation += f"{root}**{power} * "
#         number //= root ** power

#     notation += str(number)

#     return notation

# # Example usage
# number = 1234567890  # Example number
# compressed_notation = compress_to_custom_notation(number)
# print(compressed_notation)

# # print(2**1 * 3**2 * 5**1 * 3607**1 * 3803**1 * 1)
# print(2*3**2*5*3607*3803)
# print(2*3**2*5)
# print(90*3607*3803)


def compress_to_compact_notation_with_exponents(number):
    if number == 0:
        return "0"

    notation = ""

    # Handle negative numbers
    if number < 0:
        notation += "-"
        number = abs(number)

    factors = []

    while number >= 2:
        root = 2
        while number % root != 0:
            root += 1
        power = 0

        while number % (root ** (power + 1)) == 0:
            power += 1

        if power > 1:
            factors.append(f"{root}^{power}")
        else:
            factors.extend([str(root)] * power)

        number //= root ** power

    notation += "*".join(factors)

    return notation

# Example usage
number = 12345678933330  # Example number
compressed_notation = compress_to_compact_notation_with_exponents(number)
print(compressed_notation)