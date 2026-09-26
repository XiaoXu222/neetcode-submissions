class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}

        def dfs(i):
            if i >= len(s):
                return 1
            
            if s[i] == '0':
                return 0
            
            if i in cache:
                return cache[i]
            
            if i + 1 >= len(s) or int(s[i]) > 2 or (int(s[i]) == 2 and int(s[i + 1]) > 6):
                cache[i] = dfs(i + 1)
                return cache[i]
               
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        
        return dfs(0)

                
            

                    
        