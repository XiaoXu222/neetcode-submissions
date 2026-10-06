class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, s):
            if s == target:
                res.append(cur.copy())
                return
            if s > target:
                return
            
            for j in range(i, len(nums)):
                s += nums[j]
                cur.append(nums[j])
                dfs(j, cur, s)
                cur.pop()
                s -= nums[j]
            
        dfs(0, [], 0)
        return res

            

        