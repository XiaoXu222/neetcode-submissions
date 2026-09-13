class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curSet = []

        def dfs(i, curSet, res):
            if sum(curSet) == target:
                res.append(curSet.copy())
                return
            elif sum(curSet) > target or i > len(nums) - 1:
                return

            for j in range(i, len(nums)):
                curSet.append(nums[j])
                dfs(j, curSet, res)
                curSet.pop()

        dfs(0, curSet, res)
        return res
        
        