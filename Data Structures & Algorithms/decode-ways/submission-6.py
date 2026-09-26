class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                continue

            if i + 1 >= len(s) or int(s[i]) > 2 or (int(s[i]) == 2 and int(s[i + 1]) > 6):
                dp[i] = dp[i + 1]
                continue
            
            dp[i] = dp[i + 1] + dp[i + 2]
        
        return dp[0]
            