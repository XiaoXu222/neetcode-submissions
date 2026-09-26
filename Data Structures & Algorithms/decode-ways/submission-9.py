class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0,1,0]

        for i in range(len(s) - 1, -1, -1):
            tmp1 = dp[0]
            tmp2 = dp[1]

            if s[i] == '0':
                dp[2] = dp[1]
                dp[1] = 0
                dp[0] = 0
                continue
    
            if i + 1 >= len(s) or int(s[i]) > 2 or (int(s[i]) == 2 and int(s[i + 1]) > 6):
                dp[2] = dp[1]
                dp[0] = 0
                continue
            
            tmp = dp[1]
            dp[1] = dp[1] + dp[2]
            dp[2] = tmp
            dp[0] = 0
        
        return dp[1]
            