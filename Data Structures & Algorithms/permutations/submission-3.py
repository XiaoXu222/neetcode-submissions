class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i):
            if i == len(nums):
                res.append(nums[:])
                return
            
            for j in range(i, len(nums)):
                nums[j], nums[i] = nums[i], nums[j]
                dfs(i + 1)
                nums[j], nums[i] = nums[i], nums[j]
            
        dfs(0)
        return res
            