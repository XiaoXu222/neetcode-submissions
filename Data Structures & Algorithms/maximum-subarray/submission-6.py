class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        res = nums[0]
        
        for i in range(len(nums)):
            currSum = max(currSum, 0)
            currSum += nums[i]
            res = max(res, currSum)

        return res

        