class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        def dfs(i1, i2):
            if i1 == len(word1):
                return len(word2) - i2
            if i2 == len(word2):
                return len(word1) - i1
            if (i1, i2) in cache:
                return cache[(i1, i2)]
            
            if word1[i1] == word2[i2]:
                cache[(i1, i2)] = dfs(i1 + 1, i2 + 1)
            else:
                replace = 1 + dfs(i1 + 1, i2 + 1)
                remove = 1 + dfs(i1 + 1, i2)
                insert = 1 + dfs(i1, i2 + 1)
                res = min(replace, remove)
                cache[(i1, i2)] = min(res, insert)
            return cache[(i1, i2)]
        return dfs(0, 0)
            

        