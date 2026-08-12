class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans_length = len(nums) * 2
        ans = [0] * ans_length
        for i in range (ans_length):
            if i < len(nums):
                ans[i] = nums[i]
            else:
                ans[i] = nums[i-len(nums)]
        return ans
        
        