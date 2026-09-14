class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
       res = []
       curSet = []
       candidates.sort()
       
       def dfs(i, total):
            if total == target:
                res.append(curSet.copy())
                return
            elif total > target or i >= len(candidates):
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                curSet.append(candidates[j])
                dfs(j + 1, total + candidates[j])
                curSet.pop()
                
                

       dfs(0, 0)
       return res

        