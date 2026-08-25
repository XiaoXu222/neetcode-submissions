import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sumBnn = sum(piles)
        kMin = math.ceil(sumBnn / h)
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / kMin)
        if hours <= h:
            return kMin
        
        l, r = kMin + 1, max(piles)
        res = 0
        while l <= r:
            k = l + (r - l) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours > h:
                l = k + 1
            else:
                res = k
                r = k - 1
        return res
  


            
















        # # if len(piles) == h:
        # #     return max(piles)
        
        # # piles.sort()
        # l, r = 1, max(piles)
        # res = r
        # while l <= r:
        #     m = l + (r - l) // 2
        #     hours = 0
        #     for num in piles:
        #         hour = math.ceil(num / m)
        #         hours += hour
        #     if hours <= h:
        #         res = m
        #         r = m - 1
        #     elif hours > h:
        #         l = m + 1
        #     # else:
        #     #     return m

        # return res

                



        
  





         
        