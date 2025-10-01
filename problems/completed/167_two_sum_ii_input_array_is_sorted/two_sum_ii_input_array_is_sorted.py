
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

''' 
Descr.

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.



EXAMPLE 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
'''

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        compressed_list = self.listCompressor(numbers)
        for a in compressed_list:
            b = target-a
            if b in compressed_list:
                if a == b:
                    return numbers.index(a)+1, numbers.index(b)+2    
                return numbers.index(a)+1, numbers.index(b)+1
                
    def listCompressor(self, numbers:list[int]) -> list[int]:
            _numbers = numbers.copy()
            compressed_list = []
            limit = 0 
            while limit < 2:
                limit += 1
                for i in sorted(set(_numbers)):
                    if i in _numbers:
                        _numbers.remove(i)
                        compressed_list.append(i)
                if limit == 2:
                    break
            return compressed_list
    

    def listCompressor(self, numbers:list[int]) -> list[int]:
            _numbers = numbers.copy()
            compressed_list = []
            for x in range(2):
                for i in sorted(set(_numbers)):
                    if i in _numbers:
                        _numbers.remove(i)
                        compressed_list.append(i)
            return compressed_list
    

    def listCompressor(self, numbers:list[int]) -> list[int]:
            _numbers = numbers.copy()
            return [i for i in sorted(set(_numbers)) if i in _numbers]


'''
THOUGHT PROCESS:
    compressed_list = "list of one of each item in numbers x2 (2 is the max combo for possible answers)"
    index_list = "list of number of iterations of item in numbers excluding the items in compressed_list"

    example_numbers= [1,1, 2,2,2, 4, 6] 

    x,y = "the index for first number that adds to target, and the second one",None
    a,b = "the combo-numbers that when added together becomes target, and that we need to find index to",None
        
        """ 
        if a = 2, then to find the index (x) we need to:
            1: count indices in compressed_list from start to a's position. => x_1
            2. find a's represented position in the index_list and then add the indices from start to a's represented position together => x_2
            3. x_1 + x_2 = x -> the index for a

            Note. since we cannot remove "a" from the compressed list when its picked since it would mess up the index-order. 
            write a rule that says: if the number chosen in compressed list is the same as the previously chosen item, then skip. 
        """

        """ TRAIL 1:
            1. pick a from compressed_list 
            2. find the diff between target - a = c 
            3. check if c is in compressed_list, continue else skip
            *4. then proceed to find the index to "a" (x)
            *5. then find the index to "b" (y)

                *: since we saved alot of time finding the correct answer, 
                    we can make it easier by looking for the index (x,y) in the traditional way (by searching in numbers)
        """
'''
                      

def getTestCase():
    return  [
        [
            [2,2,2,2,2,2,7,7,7,7,11,11,11,11,15],
            9,
        ],
        
        [
            [2,3,4],
            6,
        ],

        [
            [-1,0],
            -1,
            ],
        
        [
            [2,7,11,15],
            9,
        ],

        [   
            [
                0,0,0,0,0,2,3,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9
            ],
            5,
        ],

        [
            [0,0,3,4],
            0,            
        ],
    ]
s = Solution()
case_nr = 0 
for (numbers, target) in getTestCase():
    case_nr += 1
    answer = s.twoSum(numbers, target)
    print()
    print(f"{case_nr}: {answer}")
    





























# # NOTE: Time Limit Exceeded -> 18/23 testcases passed. 
# class Solution:
#     def twoSum(self, numbers: list[int], target: int) -> list[int]:
#         numbers_short, index_list = self.listCompressor(numbers)
#         return self.findCombo(numbers, numbers_short, index_list, target)
    
#     def listCompressor(self, numbers:list[int]) -> list[int]:
#         checklist:set = sorted(set(numbers))
#         numbers_short = [] #shortened list of numbers, containing only two iterations. 
#         temp_x = []
#         index_list = []

#         # print("before start:")
#         # print(f"max_index: {len(numbers)+1}")
#         # print(numbers)
#         # print(checklist)
#         # print(numbers_short)
#         # print(temp_x)
#         # print("_"*50)
#         # print()


#         # NOTE: you need to include the len of deleted numbers, it will be the index addon for the next iteration. 
#         for i in checklist:
#             for x in numbers:
#                 diff = 0
#                 if x == i:
#                     temp_x.append(x)
#                     diff += 1 
#                 # if len(temp_x) == 2 or x != i:
#                     numbers_short = numbers_short + temp_x
#                     len_numbers = len(numbers)
#                     numbers = list(filter(lambda a: a != x, numbers))
#                     diff = (len_numbers - (len(numbers)))
#                     index_list.append(diff)
#                     temp_x.clear()
#                     break

#             numbers_short = numbers_short + temp_x
#         if len(checklist) != len(index_list): index_list.append(1)
#         # print(f"numbers_short: {numbers_short}")
#         # print(f"index_list: {index_list}")
#         return numbers_short, index_list

#     def findCombo(self, numbers, numbers_short: list[int], index_list:list[int], target: int) -> list[int]:
#         X = 0
#         Y = 0 
#         for b, base in enumerate(numbers_short):
#             for a, add in enumerate(numbers_short):
#                 if a == b: continue
#                 Y = a + sum(index_list[:b])
#                 if target == base + add:
#                     # if add != numbers_short[-1]: return [X + 1, X+a+1]
#                     # if add != numbers_short[-1]: return [X + 1, Y+a ]
#                     if X == 0:
#                         return [X + 1, X+a+1 ] 
#                     if add != numbers_short[-1]: return [X + 1, X+a ]
#                     else: return [X + 1, Y + 1]
#             X = index_list[b]

       
#         for i_base, base in enumerate(numbers):
#             for i_add, add in enumerate(numbers):
#                 if i_add==i_base: continue
#                 if target == base+add: return [i_base+1, i_add+1]
                
                
                
                
# # from collections import Counter

# # # NOTE: Time Limit Exceeded -> 18/23 testcases passed. 

# # class Solution:
# #     def twoSum(self, numbers: list[int], target: int) -> list[int]:
# #         numbers = Counter(numbers)
# #         print(numbers)
# #         num_list = [i for i in numbers.keys()]
# #         index_list = [i for i in numbers.values()]
# #         print(num_list)
# #         print(index_list)
# #         print("_"*50)
# #         i = 0  
# #         for val, len in numbers.items():
# #             print()
# #             i += 1
            
# #             # if len > 1:
# #             #     if val * 2 == target:
# #             print(num_list[:i])
# #             vals = [value for key, value in numbers.items()  if value in num_list[:i]]
# #             print("vals: ", vals)
# #             break
                    
# #             # if val*2 == target
    
# #             print(val, len)
    

# # testcase = [
# #     # [[2,2,2,2,2,2,7,7,7,7,11,11,11,11,15],
# #     # 9],
# #     # [[2,3,4],
# #     # 6],
# #     # [[-1,0],
# #     # -1],
# #     # [
# # #    [[2,7,11,15],
# # #     9],
# #     [   
# #         [
# #             0,0,0,0,0,2,3,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9
# #         ],
# #         5,
# #     ],
# # ]
# # s = Solution()
# # for (numbers, target) in testcase:
# #     answer = s.twoSum(numbers, target)
# #     print()
# #     print(answer)
# #     break

































# # # # https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# # # ''' 
# # # Descr.

# # # Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# # # Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# # # The tests are generated such that there is exactly one solution. You may not use the same element twice.

# # # Your solution must use only constant extra space.



# # # EXAMPLE 1:
# # # Input: numbers = [2,7,11,15], target = 9
# # # Output: [1,2]
# # # Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
 
# # # '''

# # # # NOTE: Time Limit Exceeded -> 18/23 testcases passed. 
# # # class Solution:
# # #     def twoSum(self, numbers: list[int], target: int) -> list[int]:
# # #         numbers_short, index_list = self.listCompressor(numbers)
# # #         return self.findCombo(numbers_short, index_list, target)
    
# # #     def listCompressor(self, numbers:list[int]) -> list[int]:
# # #         checklist:set = sorted(set(numbers))
# # #         numbers_short = [] #shortened list of numbers, containing only two iterations. 
# # #         temp_x = []
# # #         index_list = []

# # #         # print("before start:")
# # #         # print(f"max_index: {len(numbers)+1}")
# # #         # print(numbers)
# # #         # print(checklist)
# # #         # print(numbers_short)
# # #         # print(temp_x)
# # #         # print("_"*50)
# # #         # print()


# # #         # NOTE: you need to include the len of deleted numbers, it will be the index addon for the next iteration. 
# # #         for i in checklist:
# # #             for x in numbers:
# # #                 diff = 0
# # #                 if x == i:
# # #                     temp_x.append(x)
# # #                     diff += 1 
# # #                 # if len(temp_x) == 2 or x != i:
# # #                     numbers_short = numbers_short + temp_x
# # #                     len_numbers = len(numbers)
# # #                     numbers = list(filter(lambda a: a != x, numbers))
# # #                     diff = (len_numbers - (len(numbers)))
# # #                     index_list.append(diff)
# # #                     temp_x.clear()
# # #                     break

# # #             numbers_short = numbers_short + temp_x
# # #         if len(checklist) != len(index_list): index_list.append(1)
# # #         # print(f"numbers_short: {numbers_short}")
# # #         # print(f"index_list: {index_list}")
# # #         return numbers_short, index_list

# # #     def findCombo(self, numbers_short: list[int], index_list:list[int], target: int) -> list[int]:
# # #         X = 0
# # #         Y = 0 
# # #         for b, base in enumerate(numbers_short):
# # #             for a, add in enumerate(numbers_short):
# # #                 if a == b: continue
# # #                 Y = a + sum(index_list[:b])
# # #                 print("Y: ",Y)
# # #                 print("a: ",a)
# # #                 if target == base + add:
# # #                     if add != numbers_short[-1]: return [X + 1, Y+a ]
# # #                     else: return [X + 1, Y + 1]
# # #             X = index_list[b]
        
# # #         for i_base, base in enumerate(numbers):
# # #             for i_add, add in enumerate(numbers):
# # #                 if i_add==i_base: continue
# # #                 if target == base+add: return [i_base+1, i_add+1]

                
# # #             # print(f"base: {base}, b:{b} -> new base_i: {b + index_list[b]} ({b} + {index_list[b]})")
# # #             #     # add_i += sum(index_list[:b])
# # #                 # print(f"base: {base}, add: {add}, a:{a} -> new a: {Y} ")
# # #             #     # add_i += index_list[add_i]
# # #                 # print()

# # # '''
# # # mitt svar:  [2,3]
# # # fasit:      [6,7]
# # # '''







# # #     # def listCompressor(self, numbers:list[int]) -> list[int]:

# # #     #     '''
# # #     #     NEWNEW plan; since the answert can only contain two integers (a+b)
# # #     #     then we can remove all iterations that exceeds 2 interations. 
# # #     #     [1,1,1,1,2,2] --> [1,1,2,2] since we will never be able to use more than two 1's.

# # #     #     1. make set of list, this will be the checker to see what the list contains. 
# # #     #     2. iterate the list starting from set[0] append the two first iterations to a new list, then jump to the next set item set[2].
# # #     #         continue till done.
# # #     #     3. then proceed with the normal twosum formula.    

        
# # #     #     '''


# # #     #     checklist:set = sorted(set(numbers))
        
# # #     #     numbers_short = [] #shortened list of numbers, containing only two iterations. 
# # #     #     temp_x = []

# # #     #     print("before start:")
# # #     #     print(numbers)
# # #     #     print(checklist)
# # #     #     print(numbers_short)
# # #     #     print(temp_x)
# # #     #     print("_"*50)
# # #     #     print()


# # #     #     for i in checklist:
# # #     #         print(f"CHECK NUMBER: {i}")
# # #     #         print(f"numbers: {numbers}")
# # #     #         print(f"checklist: {checklist}")
# # #     #         for x in numbers:
# # #     #             print(f"TEST NUMBER: {i}")

# # #     #             if x == i:
# # #     #                 temp_x.append(x)

# # #     #             if len(temp_x) == 2 or x != i:
# # #     #                 print(f"temp_x: {temp_x}")
# # #     #                 numbers_short = numbers_short+temp_x
# # #     #                 temp_x.clear()
# # #     #                 numbers = list(filter(lambda a: a != x, numbers))
                    
# # #     #                 break
# # #     #         print("-"*20)

# # #     #             # numbers = list(filter(lambda a: a != x, numbers)) #removes x from list when were done with it, to save time. 
                
# # #     #         numbers_short = numbers_short+temp_x
# # #     #     print(f"temp_x: {numbers_short}")
# # #     #     print("\n DONE \n", ("="*50))
# # #     #     return numbers_short

