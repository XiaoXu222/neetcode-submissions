class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        l = 0
        res = 1
        prev = {}
        for r in range(len(s)):
            if s[r] in prev:
                l = max(l, prev[s[r]] + 1)
                
            prev[s[r]] = r
            res = max(res, r - l + 1)

        return res

        