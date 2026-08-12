class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_s, map_t = {}, {}

        for char_s, char_t in zip(s, t):
            map_s[char_s] = map_s.get(char_s, 0) + 1
            map_t[char_t] = map_t.get(char_t, 0) + 1
        
        return map_s == map_t
            

        # hashmap_1 = {}
        # for charct in s:
        #     if charct in hashmap_1:
        #         hashmap_1[charct] += 1
        #     else:
        #         hashmap_1[charct] = 1

        # hashmap_2 = {}
        # for charct in t:
        #     if charct in hashmap_2:
        #         hashmap_2[charct] += 1
        #     else:
        #         hashmap_2[charct] = 1
        
        # if hashmap_1 == hashmap_2:
        #     return True
        # else return False
        
        


        