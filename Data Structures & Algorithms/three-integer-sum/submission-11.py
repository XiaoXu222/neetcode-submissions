class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        indicies = defaultdict(list)
        for i in range(len(nums)):
            indicies[nums[i]].append(i)

        res = set()
        for i in range(0,len(nums)-2):
            for j in range(i+1,len(nums)):
                third = -(nums[i] + nums[j])
                if third in indicies:
                    for k in indicies[third]:
                        if k != i and k != j:
                            res.add(tuple(sorted([nums[i], nums[j], nums[k]]))) 

        if res:
            res = list(res)
            res = [list(t) for t in res]
        
        return list(res)
            
                    

        