class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] >= nums[0]:
            return nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2

            if m - 1 < 0 and len(nums) == 2:
                return nums[-1]
            elif nums[m - 1] > nums[m]:
                return nums[m]
            
            if nums[m] >= nums[l] and nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m - 1
        

        