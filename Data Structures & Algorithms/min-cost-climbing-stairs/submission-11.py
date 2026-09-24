class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [cost[0], cost[1]]
        i = 2
        while i < len(cost):
            tmp = dp[1]
            dp[1] = cost[i] + min(tmp, dp[0])
            dp[0] = tmp 
            i += 1
        
        return min(dp[0], dp[1])

        