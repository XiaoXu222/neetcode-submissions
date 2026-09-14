class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):
            if i == len(nums):
                return [[]]
            perms = dfs(i + 1)
            res = []
            for p in perms:
                for j in range(len(p) + 1):
                    pcopy = p.copy()
                    pcopy.insert(j, nums[i])
                    res.append(pcopy)
            return res
        
        return dfs(0)
        