class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(i):
            if i == n + 1:
                return [""]
            perms = dfs(i + 1)
            res = set()
            for p in perms:
                for j in range(len(p) + 1):
                    pcopy = p[:j] + "()" + p[j:]
                    res.add(pcopy)
            return res

        return list(dfs(1))
            

        


        