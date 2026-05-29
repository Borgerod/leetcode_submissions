# class Solution:
    # def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
    #     '''
    #     n : counter - banana piles
    #     i : index for banana piles in piles
    #     piles[i] : amount of bananas in pile
    #     h : time limit (counter - hours)
    #     k : eating speed (bananas per hour)
    #     iteration: per hour.
    #     1. pick a banana pile
    #     2. eat 'k' bananas from it
    #     if len(piles[i]) < k : eats all, then break. (she will NOT move to another pile)

    #     return, the smallest 'k' possible that allows all bananas to be eaten (within 'h' iterations). 
    #     '''
    #     # k = 10 #speed (placeholder number for now)
    #     # start_off_point = len(piles)/h #simplest approach.
    #     # k = start_off_point 
    #     # for _ in h:

    #     #     if piles[i] <= k: 
    #     #         piles[i] = 0
    #     #         continue
            
    #     #     piles[i] -= k

    #     print(f"piles before: {piles}")
    #     piles.sort()

    #     print(f"piles after: {piles}")
        
    #     start_off_point = sum(piles)//h #simplest approach.
    #     print(f"total bananas: {sum(piles)}")
    #     print(f"start_off_point: {start_off_point}")
    #     k = start_off_point 
    #     n = len(piles)

    #     # # find midpoint, or else pick mid-left

        
    #     # rules:
    #     #     k_min > piles[0]
    #     #     k_max < piles[-1]
    #     #     k_optimal <= h
    #     #     k_optimal >= k_min and <= k_max

    #     # while k >= k_min:
    #     i = (n//2)
    #     k = piles[i]
    #     lead_k = None
    #     piles_copy = piles.copy()
        
    #     h_copy = h
    #     max_k = piles[-1]
    #     min_k = piles[0]
    #     print(max_k)
    #     while k <= max_k or k >= min_k:
    #         piles = piles_copy.copy() 

    #         h=h_copy
    #         n = len(piles)
    #         i = (n//2)
            

    #         print(f"")
    #         print(f"k : {k}")
    #         print(f"  piles :{piles}")
    #         print(f"  h:{h}")
    #         print(f"  i:{i}")
    #         print(f"  k:{k}")
    #         print(f"  n:{n}")
    #         print(f"_______")
            
    #         while h > 0 or n > 0:
    #             print(f"    h:{h}")
                
    #             print(f"     i:{i}")
    #             print(f"     k:{k}")
    #             print(f"     n:{n}")
                
    #             if piles[i]<=k:
    #                 piles.pop(i)
    #                 n -= 1
    #                 i = (n//2)
    #             else:
    #                 piles[i]-=k
    #             print(f"     pile prog: {piles} | {h} hours left")
    #             h-=1

    #             if not n or h == 0: 
    #                 break
            

    #         # if n != 0 
    #         if h==0 and n>0:
    #             # too small
    #             print("too small")
    #             # print("is the too-small-k smaller the lead?")
    #             # if lead_k and k < lead_k:
    #             if lead_k and k+1 == lead_k:
    #                 print(f"allready tried {lead_k}, end search")
    #                 return lead_k
    #             else:
    #                 # print("     too small -> returning lead_k")
    #                 lead_k = k
    #                 piles = piles_copy.copy() 
    #                 k+=1
    #                 print(f"    New lead :{lead_k}")
    #                 print(f"    current k :{k}")
    #                 # return lead_k
    #             # break
    #         elif h>=0 and n==0:
    #             # (maybe) too big
    #             print("     (maybe) too big")
    #             if lead_k and k > lead_k:
    #             # if lead_k and k-1 == lead_k:
    #                 print(f"    allready tried {lead_k}, return {k} end search")
    #                 return k
    #             # if lead_k and k-1 != lead_k:
    #             #     print(f"    not tried {lead_k} end search")
    #             #     return lead_k
    #             else:
    #                 lead_k = k
    #                 piles = piles_copy.copy() 
    #                 k-=1
    #                 print(f"    New lead :{lead_k}")
    #                 print(f"    current k :{k}")
    #             # break
    #         elif k >= max_k:
    #             print("  bigger than max")
    #             break
    #         elif k <= min_k:
    #             print("  smaller than min")
    #             break
    #         print(f"current k :{k}")
    #         print(f"current lead k :{lead_k}")
    #         piles = piles_copy.copy() 
    #         # piles = piles_copy.copy() 
    #         # k = piles[i]
    #         # k -= 1

    #     # return None

class Solution:
    ''' ORIGINAL '''

    def test(self, piles, k, h):
        for pile in piles:
            h -= (pile + k - 1) // k
            if h < 0:
                return False
        return True
        
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        ''' seperating for cleanliness sake '''

        left = 1
        right = max(piles)
        n = len(piles)
        # note: k = mid

        if h==n: #edge cases to save time
            return max(piles)
        
        if n==1: #edge cases to save time
            return (piles[0] + h - 1) // h

        while left <= right:
            mid = (left + right) // 2
            if self.test(piles, mid, h,):
                right = mid - 1
            else:
                left = mid + 1
        return left

class Solution:
    ''' MERGED '''
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        ''' seperating for cleanliness sake '''

        left = 1
        right = max(piles)
        n = len(piles)
        # note: k = mid

        if h==n: #edge cases to save time
            return max(piles)
        
        if n==1: #edge cases to save time
            return (piles[0] + h - 1) // h

        while left <= right:
            _h = h
            mid = (left + right) // 2
            for pile in piles:
                _h -= (pile + mid - 1) // mid
            if _h < 0: 
                left = mid + 1
            else: 
                right = mid - 1
        return left

            

if __name__ == '__main__':

    cases = [
        # [3,6,7,11],
		# 8,
		# [30,11,23,4,20],
		# 5,
		# [30,11,23,4,20],
		# 6
    [1000000000],
1000000000,
    ]

#> OPTION 2 (FOR MULTIPLE INPUTS)
    s = Solution()
    for i in range(0, len(cases), 2):

        piles = cases[i+0]
        h = cases[i+1]
        print(f"___ NO.{i} ___________________________________")
        print(f"Input: piles={(str(piles[:10])[:-1] + f', ... {piles[-1]}]') if isinstance(piles, list) and len(piles) > 10 else piles}, h={(str(h[:10])[:-1] + f', ... {h[-1]}]') if isinstance(h, list) and len(h) > 10 else h}")
        ans = s.minEatingSpeed(piles, h)
        print(f"Output: {ans}\n")



"""
expectations: 
1:4
2:30
3:23
"""


"""
__ GITHUB PUSH COMMENT _________________________
Finish 875. Koko Eating Bananas + move to completed
contains: description, solution.
difficulty: Medium
topics: Array, Binary Search
"""