class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = defaultdict(int)
        for c1 in s1:
            countS1[c1] += 1
        countS2 = defaultdict(int)
        l = 0
   
        for r in range(len(s2)):
            countS2[s2[r]] += 1
            if r - l + 1 > len(s1):
                countS2[s2[l]] -= 1
                if countS2[s2[l]] == 0:
                    del countS2[s2[l]]
                l += 1
            if r - l + 1 == len(s1):
                if countS2 == countS1:
                    return True
        return False

        
        