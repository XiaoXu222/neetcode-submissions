class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans_length = len(nums) * 2
        ans = [0] * ans_length
        for i, num in enumerate(nums):
            ans[i] = ans[i + len(nums)] = num
        return ans
        # for i in range (len(nums)):
        #     ans[i] = nums[i]
        #     ans[i+len(nums)] = nums[i]
        # return ans
        
        