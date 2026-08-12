import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        
        piles.sort()
        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = l + (r - l) // 2
            hours = 0
            for num in piles:
                hour = math.ceil(num / m)
                hours += hour
            if hours <= h:
                res = m
                r = m - 1
            elif hours > h:
                l = m + 1
            # else:
            #     return m

        return res

                



        
  





         
        