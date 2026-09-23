class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [nums[0], max(nums[0], nums[1])]
        i = 2
        while i <= len(nums) - 1:
            tmp = dp[1]
            dp[1] = max(tmp, nums[i] + dp[0])
            dp[0] = tmp
            i += 1
        return dp[1]
        