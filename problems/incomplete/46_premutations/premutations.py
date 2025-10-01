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

nums = [0,1]
s = Solution()
result = s.permute(nums)
print(result)