class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        compressed_list = nums
        print("nums: ",compressed_list, len(compressed_list),"\n")
        combinations = []
        for a in compressed_list:
            compressed_list_copy = compressed_list.copy()
            compressed_list_copy.remove(a)
            print(f"a ({a}) removed: {compressed_list_copy}", len(compressed_list_copy))
            for b in compressed_list_copy:
                if b in compressed_list_copy:
                    compressed_list_copy.remove(b)
                    print(b)
                    for c in compressed_list_copy:
                        if c in compressed_list_copy:
                            print("     ",a,b,c)
            print("-"*20)
        #         if b in compressed_list_copy:
        #             compressed_list_copy.remove(b)
        #             print(f"    b ({b}) removed: {compressed_list_copy}", len(compressed_list_copy))
            
        #             # c = -sum((a, b))
        #             # print(c, a,b , "=>", -sum((a, b)))
        #             for c in compressed_list_copy:
        #                 if c in compressed_list_copy:
        #                     print(f"        c ({c}) was found in list:{ compressed_list_copy}")
        #                     # print(compressed_list_copy)
        #                     combinations.append(sorted([a,b,c]))
        #     print("-"*20)
        # return list(set(tuple(sorted(sub)) for sub in combinations))
                    






    # def listCompressor(self, numbers:list[int]) -> list[int]:
    #         _numbers = numbers.copy()
    #         compressed_list = []
    #         limit = 0 
    #         while limit < 3:
    #             limit += 1
    #             for i in sorted(set(_numbers)):
    #                 if i in _numbers:
    #                     # print(i)
    #                     _numbers.remove(i)
    #                     compressed_list.append(i)
    #             if limit == 2:
    #                 break
    #         return compressed_list

def getTestCase():
    return  [
        # [0,0,0]
        [-5,0,-2,3,-2,1,1,3,0,-5,3,3,0,-1],
        # [-1,0,1,2,-1,-4],
        # [0,1,1],
        # [0,0,0,1],
    ]
s = Solution()
case_nr = 0 
for (numbers) in getTestCase():
    case_nr += 1
    answer = s.threeSum(numbers)
    print()
    print(f"{case_nr}: {answer}")
    break
    










