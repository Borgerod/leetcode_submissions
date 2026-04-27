class Solution:
	def permute(self, nums: list[int]) -> list[list[int]]:
		res = [[]]
		for num in nums:
			length = len(res)
			for i in range(length):
				subset = res[i]
				for j in range(len(subset)):
					res.append(subset[:j] + [num] + subset[j:])
				subset.append(num)
		return res
    

if __name__ == '__main__':

    cases = [
        [1,2,3],
		[0,1],
		[1],
    ]

#> OPTION 1 (FOR SINGLE INPUTS)
    s = Solution()
    for i, nums in enumerate(cases):
        print(f"___ NO.{i} ___________________________________")
        print(f"Input: nums={(str(nums[:10])[:-1] + f', ... {nums[-1]}]') if isinstance(nums, list) and len(nums) > 10 else nums}")
        ans = s.permute(nums)
        print(f"Output: {ans}\n")



"""
(NEW) TESTCASES:
cases = [
    '[1,2,3]',
    '[0,1]',
    '[1]',
    [1, 2, 3],
]

FOR LEETCODE:
'[1,2,3]'
'[0,1]'
'[1]'
[1, 2, 3]
"""


"""
__ GITHUB PUSH COMMENT _________________________
Finish 46. Permutations + move to completed
contains: description, solution.
difficulty: Medium
topics: Array, Backtracking
"""