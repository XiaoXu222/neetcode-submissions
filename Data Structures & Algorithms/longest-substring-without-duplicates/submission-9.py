class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        noDu = set()

        for r in range(len(s)):
            while s[r] in noDu:
                
                noDu.remove(s[l])
                l += 1
            noDu.add(s[r])
            res = max(res, r - l + 1)

        return res


        
        