class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char)-ord('a')] += 1
            count_tup = tuple(count)
            if count_tup in freq:
                freq[count_tup].append(word)
            else:
                freq[count_tup] = []
                freq[count_tup].append(word)
        
        groups = []
        for value in freq.values():
            groups.append(value)
        return groups



        

        