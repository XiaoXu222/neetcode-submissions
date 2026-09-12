class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, curSet = [], []

        # def helper(i, nums, curSet, subsets):
        def helper(i):
            if i == len(nums):
                subsets.append(curSet.copy())
                return
            curSet.append(nums[i])
            # helper(i + 1, nums, curSet, subsets)
            helper(i + 1)
            curSet.pop()
            # helper(i + 1, nums, curSet, subsets)
            helper(i + 1)

        
        # helper(0, nums, curSet, subsets)
        helper(0)
        return subsets
    