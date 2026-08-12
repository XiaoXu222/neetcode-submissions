class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans_length = len(nums) * 2
        ans = [0] * ans_length
        for i in range (len(nums)):
            ans[i] = ans[i+len(nums)] = nums[i]
        return ans
        
        