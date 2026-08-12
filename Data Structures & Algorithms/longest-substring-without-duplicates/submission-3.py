class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if not s:
        #     return 0
        # elif s and len(s) == 1:
        #     return 1

        string = defaultdict(int)
        res = 0
        l = 0

        for r in range(len(s)):
            if l != r and s[r] in string:
                l = max(l, string[s[r]] + 1)
            string[s[r]] = r
            res = max(res, r - l + 1)
        
        return res
            



        


        