

class Solution:
    ''' MERGED '''
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        ''' seperating for cleanliness sake '''
        _max = max(piles)
        left = 1
        right = _max
        n = len(piles)
        # note: k = mid

        if h==n: #edge cases to save time
            return _max
        
        if n==1: #edge cases to save time
            return (piles[0] + h - 1) // h

        while left <= right:
            _h = h
            mid = (left + right) // 2
            for pile in piles:
                _h -= (pile + mid - 1) // mid
                # _h += math.ceil(pile / mid) #alternative, makes it a tier more memory efficiant. 
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
		# 6,
        # [1000000000],
        # 1000000000,

        # [1000000000],
        # 1,
        # [1, 1, 1, 1, 1],
        # 5,
        # [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],
        # 5,
        # [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],
        # 1000000000,
        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        # 10,
        # [1, 1000000000, 1, 1000000000, 1, 1000000000],
        # 6,
        # [1, 1000000000, 1, 1000000000, 1, 1000000000],
        # 1000000000,
        [312884470],
312884469,
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


