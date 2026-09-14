class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curSet = []
        total = 0
        nums.sort()

        def dfs(i, total):
            if total == target:
                res.append(curSet.copy())
                return
            elif total > target or i > len(nums) - 1:
                return

            for j in range(i, len(nums)):
                curSet.append(nums[j])
                dfs(j, total + nums[j])
                curSet.pop()

        dfs(0, 0)
        return res
        
        