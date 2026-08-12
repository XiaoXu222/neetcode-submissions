class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_1 = {}
        for charct in s:
            if charct in hashmap_1:
                hashmap_1[charct] += 1
            else:
                hashmap_1[charct] = 1

        hashmap_2 = {}
        for charct in t:
            if charct in hashmap_2:
                hashmap_2[charct] += 1
            else:
                hashmap_2[charct] = 1
        
        if hashmap_1 == hashmap_2:
            return True
        else:
            return False
        
        


        