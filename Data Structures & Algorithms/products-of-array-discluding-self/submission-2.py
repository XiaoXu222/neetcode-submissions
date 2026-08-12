class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        prod_pre = 1
        for i in range(1,len(nums)):
            prod_pre *= nums[i-1]
            prefix.append(prod_pre)
        
        suffix = [1]
        prod_suf = 1
        for j in range(-2,-len(nums)-1,-1):
            prod_suf *= nums[j+1]
            suffix.append(prod_suf)
        
        res = []
        for i in range(len(nums)):
            j = len(nums) - 1 - i
            res.append(prefix[i]*suffix[j])
        return res

        
         
        

            
        