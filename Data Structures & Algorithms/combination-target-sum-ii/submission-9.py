class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, cur, s):
            if s == target:
                res.append(cur.copy())
                return
            if s > target:
                return
            
            for j in range(i, len(candidates)):
                if candidates[j - 1] == candidates[j] and j - 1 >= i:
                    continue
                s += candidates[j]
                cur.append(candidates[j])
                dfs(j + 1, cur, s)
                cur.pop()
                s -= candidates[j]
            
        dfs(0, [], 0)
        return res

            

        