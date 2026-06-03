# class Solution:
 
#     def search(self, nums: list[int], target: int) -> int:
#         ''' MERGED '''
#         left = 0
#         right = len(nums) - 1
#         t=-1
#         while left<right:
#             mid = left + ((right - left) // 2)
#             print(f"    split:  {nums[left:mid]} {nums[mid]} {nums[mid:right]}")
            
#             if nums[mid] > nums[right] or nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1

#             if nums[mid] == target:
#                 t = mid
#         return t
class Solution:
    def findMin(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:

            mid = left + ((right - left) // 2)

            if nums[mid] > nums[right]:
                left = mid + 1
            
            elif nums[mid] < nums[right]:
                right = mid    
        return left
    
    def binarySearch(self, arr, targetVal):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == targetVal:
                return mid

            if arr[mid] < targetVal:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        rotation = self.findMin(nums, target)
        _nums = nums[rotation:] + nums[:rotation]
        ans = self.binarySearch(_nums, target)
        if ans == -1:
            return -1
        return (ans + rotation) % n
    
if __name__ == '__main__':

    cases = [
        [4,5,6,7,0,1,2],
		0,
		[3,5,6,0,1,2],
        5,
		# [4,5,6,7,0,1,2],
		# 3,
		# [1],
		# 0
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