class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(i):
            if i == len(nums):
                return [[]]
            res = []
            cur = dfs(i + 1)
            for each in cur:
                for j in range(len(each) + 1):
                    eachC = each.copy()
                    eachC.insert(j, nums[i])
                    res.append(eachC)
            return res
            
        return dfs(0)


        