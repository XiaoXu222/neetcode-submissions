class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > -num:
                    r -= 1
                elif nums[l] + nums[r] < -num:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l, r = l + 1, r - 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1


        return res
        # indicies = defaultdict(list)
        # for i in range(len(nums)):
        #     indicies[nums[i]].append(i)

        # res = set()
        # for i in range(0,len(nums)-2):
        #     for j in range(i+1,len(nums)):
        #         third = -(nums[i] + nums[j])
        #         if third in indicies:
        #             for k in indicies[third]:
        #                 if k != i and k != j:
        #                     res.add(tuple(sorted([nums[i], nums[j], nums[k]]))) 

        # if res:
        #     res = list(res)
        #     res = [list(t) for t in res]
        
        # return list(res)
            
                    

        