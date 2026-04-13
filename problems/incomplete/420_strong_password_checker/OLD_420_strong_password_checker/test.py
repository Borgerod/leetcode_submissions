import math

def shorten_to_6_digits(long_number):
    # Calculate a 6-digit number by taking the remainder when dividing by 1,000,000
    print(f"long_number : {long_number}")
    remainder = long_number % 1000000
    divided = long_number // 1000000
    print(f"remainder : {remainder}")
    print(f"divided : {divided}")
    
    return divided


def longen(short_number):
    # 123456789012345678901234567890
    long_number = 1000000*short_number
    return long_number



# Example usage
long_number = 123456789012345678901234567890  # Example long number
# shortened_number = shorten_to_6_digits(long_number)
# long_number = longen(shortened_number)




import math  # Needed to generate the best range, so you have no repeated combinations.
x = long_number

    
# lim = int(math.sqrt(long_number))
# for i in range (1, lim):
#     if long_number%i==0:
#         if len(str(i)) == len(str(long_number/i)):
#             print(i, int(long_number/i))
#             res = [i, long_number/i]
# print(res)


import math

def find_closest_length_pair(data):
    closest_item = None
    min_length_difference = float('inf')

    for item in data:
        key, value = list(item.keys())[0], list(item.values())[0]
        length_difference = abs(len(str(key)) - len(str(value)))

        if length_difference < min_length_difference:
            min_length_difference = length_difference
            closest_item = item

    return closest_item

def find_divisor_to_get_whole_number(long_number):
    candicates = []
    # start = (long_number//100)*30
    # end = (long_number//100)*70
    for x in range(1, long_number + 1):
        # if long_number % x == 0:
        if long_number % x == 0 and x!=1 and x!=2:
            print(x)
            # candicate = {x:long_number//x}
            candicates.append({x:long_number//x})
            # if len(str(x))>len(str(long_number//x)):
            #     return find_closest_length_pair(candicates)
            # print(f"{long_number}//{x} = {long_number//x} with remainding: {long_number % x}")
            # return x
    print(candicates)
    return find_closest_length_pair(candicates)
    # print(candicates)
# Examµple usage
long_number = 2617233428262364382  # Example long number
divisor = find_divisor_to_get_whole_number(long_number)
print(divisor)



def divide_by_2(self):


# def find_divisor_to_get_whole_number(long_number):
#     for x in range(1, long_number + 1):
#         if long_number % x == 0:
#             return x

# # Example usage
# long_number = 123456789  # Example long number
# divisor = find_divisor_to_get_whole_number(long_number)
# print(divisor)










# for factor_pair in factor_pairs:
#     print(factor_pair)


# print(shortened_number)

# print(long_number)
# from pprint import pprint
# from collections import defaultdict

# class Solution:
#     def isValidSudoku(self, board: list[list[str]]) -> bool:
#         for row in board:
#             if not self.check_sublist(row):
#                 return False
     
#         for col in self.get_cols(board):
#             if not self.check_sublist(col):
#                 return False

#         for box in self.get_boxes(board):
#             if not self.check_sublist(box):
#                 return False
#         return True

#     def check_sublist(self, sublist) -> bool:
#         ''' sublist: either box, row or column'''
#         int_count = 0 
#         for i in sublist:
#             if i != ".":
#                 int_count += 1
#         return len(set(sublist))-1 == int_count

#     def get_cols(self, board):
#         return [[row[i] for row in board] for i in range(0,9)]
        

#     def get_boxes(self, board):
#         mp = defaultdict(list)
#         for row, key_section in zip(board, [[1,2,3],[1,2,3],[1,2,3], [4,5,6],[4,5,6],[4,5,6], [7,8,9],[7,8,9],[7,8,9]]):
#             mp[key_section[0]].extend(row[0:3])
#             mp[key_section[1]].extend(row[3:6])
#             mp[key_section[2]].extend(row[6:9])
#         return [mp.get(i) for i in mp] 
       


# test_cases = [
# [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]],
# [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]],
# [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]],
# ]
# for i, board in enumerate(test_cases): 
#     s = Solution()
#     res = s.isValidSudoku(board)
#     print(f"results for case [{i}] : {res}")
#     print("_"*50,"\n")

    