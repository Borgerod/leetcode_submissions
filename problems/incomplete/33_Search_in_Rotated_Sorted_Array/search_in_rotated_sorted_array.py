class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        '''
        
        '''



        return None



    

if __name__ == '__main__':

    cases = [
        [4,5,6,7,0,1,2],
		0,
		[4,5,6,7,0,1,2],
		3,
		[1],
		0
    ]

#> OPTION 2 (FOR MULTIPLE INPUTS)
    s = Solution()
    for i in range(0, len(cases), 2):

        nums = cases[i+0]
        target = cases[i+1]
        print(f"___ NO.{i} ___________________________________")
        print(f"Input: nums={(str(nums[:10])[:-1] + f', ... {nums[-1]}]') if isinstance(nums, list) and len(nums) > 10 else nums}, target={(str(target[:10])[:-1] + f', ... {target[-1]}]') if isinstance(target, list) and len(target) > 10 else target}")
        ans = s.search(nums, target)
        print(f"Output: {ans}\n")



"""
(NEW) TESTCASES:
cases = [
    '[4,5,6,7,0,1,2]',
    '0',
    '[4,5,6,7,0,1,2]',
    '3',
    '[1]',
    '0',
    [1, 2, 3],
    0,
]

FOR LEETCODE:
'[4,5,6,7,0,1,2]'
'0'
'[4,5,6,7,0,1,2]'
'3'
'[1]'
'0'
[1, 2, 3]
0
"""


"""
__ GITHUB PUSH COMMENT _________________________
Finish 33. Search in Rotated Sorted Array + move to completed
contains: description, solution.
difficulty: Medium
topics: Array, Binary Search
"""