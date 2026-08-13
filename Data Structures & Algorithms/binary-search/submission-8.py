class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + ((right - left) // 2)
            # mid = (left +right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
        
        return -1





        # l, r = 0, len(nums) - 1

        # while l <= r:
        #     midInd = l + (r - l) // 2
        #     mid = nums[midInd]
        #     if mid < target:
        #         l = midInd + 1
        #     elif mid > target:
        #         r = midInd - 1
        #     else:
        #         return midInd

        # return -1
        