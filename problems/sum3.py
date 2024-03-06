from collections import defaultdict, Counter
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i + 1, len(nums)-1 #l (left) will be the one next to a, and r (right): the end of the list.
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1 #if threeSum is more than 0, r-index needs to be reduced by one. 
                elif threeSum < 0:
                    r += 1#increase r with 1 
                else:
                    res.append([a,nums[l], nums[r]]) #append solution
                    # reset the pointers (l, r)
                    l += 1 
                    while nums[l] == nums[l-1] and l>r:
                        l += 1 
        return res

s = Solution()
s.threeSum(nums=[[-1,0,1,2,-1,-4]])
print(s)


        # solution_list = []  #will contain soilutiuons
        # # solutions = defaultdict(0, "a","b","c")
        # solutions = {
        #     'a': None,
        #     'b': None,
        #     'c': None,
        # }
        # for a in nums:
        #     for s in solution_list:
        #         if s['a'] == a:
        #             nums.pop(a)
        #             continue
        #     c = nums[-1]
        #     for s in solution_list:
        #         if s['c'] == c:
        #             nums.pop(-1)
        #             continue
        #     for b in nums:
        #         for s in solution_list:
        #             if s['b'] == b:
        #                 nums.pop(-1)
        #                 continue
        #         solutions['a'],solutions['c'],solutions['c']=a,b,c
        #         solution_list.append(solutions)
        # return solution_list
    