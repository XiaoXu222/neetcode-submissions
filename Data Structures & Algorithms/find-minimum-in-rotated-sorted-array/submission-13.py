class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                return nums[mid]

            

        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     m = l + (r -l) // 2
        #     if nums[m] > nums[r]:
        #         l = m + 1
        #     elif nums[m] < nums[r]:
        #         r = m
        #     else:
        #         return nums[m]



        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     if nums[l] <= nums[r]:
        #         return nums[l]
            
        #     m = l + (r -l) // 2
        #     if nums[l] <= nums[m]:
        #         l = m + 1
        #     else:
        #         r = m

        # if nums[-1] >= nums[0]:
        #     return nums[0]

        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     m = l + (r - l) // 2

        #     if m - 1 < 0 and len(nums) == 2:
        #         return nums[-1]
        #     elif nums[m - 1] > nums[m]:
        #         return nums[m]
            
        #     if nums[m] >= nums[l] and nums[m] >= nums[r]:
        #         l = m + 1
        #     else:
        #         r = m - 1
        

        