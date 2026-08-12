class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_1 = {}
        for i in s1:
            count_1[i] = 1 + count_1.get(i, 0)

        l = 0
        count_2 = {}
        for r in range(len(s2)):
            if s2[r] not in count_1:
                l = r + 1
                count_2 = {}
            else:
                count_2[s2[r]] = 1 + count_2.get(s2[r], 0)
                if count_2[s2[r]] > count_1[s2[r]]:
                    if count_2[s2[l]] == 1:
                        del count_2[s2[l]]
                    else:
                        count_2[s2[l]] -= 1
                    l += 1

            if count_2 == count_1:
                return True

        return False


        