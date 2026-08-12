class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        L = 0

        for R in range(len(prices)):
            if prices[R] <= prices[L]:
                L = R
            else:
                res = max(res, prices[R] - prices[L])
        
        return res
            
        