class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms = [[]]
       
        for n in nums:
            res = []
            for p in perms:
                for j in range(len(p) + 1):
                    pcopy = p.copy()
                    pcopy.insert(j, n)
                    res.append(pcopy)
            perms = res
    
        return res