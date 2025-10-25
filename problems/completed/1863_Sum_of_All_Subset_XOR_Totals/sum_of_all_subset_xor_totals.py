

class Solution:
    '''
    1.1) - Compressed version
    '''
    def subsetXORSum(self, nums: list[int]) -> int:
        if len(nums)==1: return nums[0]   
        return sum([self.xor_all(sub) for sub in sorted(self.get_combinations(nums), key=len)])
    
    def xor_all(self, nums):
        result = 0
        for n in nums: result ^= n
        return result

    def get_combinations(self, lst):
        if not lst: return [[]]
        rest_combinations = self.get_combinations(lst[1:])
        return rest_combinations + [[lst[0]] + combo for combo in rest_combinations]

class Solution:
    '''
    1.1) - three steps. makes subsets, calculates xor from subsets, sum(subsets)
    '''
    def subsetXORSum(self, nums: list[int]) -> int:
        if len(nums)==1: 
            return nums[0]
        all_combinations = self.get_combinations(nums)
        sum_xor = 0
        for sub in sorted(all_combinations, key=len):
            xor = self.xor_all(sub)
            sum_xor+=xor
        return sum_xor
    

    def xor_all(self, nums):
        result = 0
        for n in nums:
            result ^= n
        return result

    def get_combinations(self, lst):
        if not lst:
            return [[]]
        first = lst[0]
        rest_combinations = self.get_combinations(lst[1:])
        with_first = [[first] + combo for combo in rest_combinations]
        return rest_combinations + with_first

class Solution:
    '''
    1.1) - three steps. makes subsets, calculates xor from subsets, sum(subsets)
    '''
    def subsetXORSum(self, nums: list[int]) -> int:
        if len(nums)==1: 
            return nums[0]
        all_combinations = self.get_combinations(nums)
        sum_xor = 0
        for sub in sorted(all_combinations, key=len):
            xor = self.xor_all(sub)
            sum_xor+=xor
        return sum_xor
    

    def xor_all(self, nums):
        result = 0
        for n in nums:
            result ^= n
        return result

    def get_combinations(self, lst):
        if not lst:
            return [[]]
        first = lst[0]
        rest_combinations = self.get_combinations(self.xor_all(lst[1:]))
        with_first = [[first] + combo for combo in rest_combinations]
        return rest_combinations + with_first
        















if __name__ == '__main__':


    cases = [
        [9],
        [1, 3],
        [5, 1, 6],
        # [3, 4, 5, 6, 7, 8],
        # [1],
        # [20],
        # [1, 20],
        # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        # [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
    ]

    #> OPTION 1 (for single inputs)
    s = Solution()
    for i, nums in enumerate(cases):
        print(f"___ NO.{i} ___________________________________")
        print(f"n={i} -> {s.subsetXORSum(nums)}\n")
    
''' #> ___ generated cases _______________________________

cases = [
    [1, 3],
    [5, 1, 6],
    [3, 4, 5, 6, 7, 8],
    [1],
    [20],
    [1, 20],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # all minimum, length=12
    [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],  # all maximum, length=12
]

print("cases = [")
for c in cases:
    print(f"    {c},")
print("]\n")

for c in cases:
    print(c)


Output:
cases = [
    [1, 3],
    [5, 1, 6],
    [3, 4, 5, 6, 7, 8],
    [1],
    [20],
    [1, 20],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
]

[1, 3]
[5, 1, 6]
[3, 4, 5, 6, 7, 8]
[1]
[20]
[1, 20]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]



'''

