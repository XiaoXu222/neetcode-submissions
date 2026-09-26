class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp0 = [nums[0], max(nums[0], nums[1])]
        dp1 = [0, nums[1]]
        return max(self.helper(dp0, len(nums) - 1, nums), self.helper(dp1, len(nums), nums))
        

    
    def helper(self, dp, end, nums):
        i = 2
        for i in range(i, end):
            tmp = dp[1]
            dp[1] = max(dp[0] + nums[i], dp[1])
            dp[0] = tmp
        return dp[1]
 

               