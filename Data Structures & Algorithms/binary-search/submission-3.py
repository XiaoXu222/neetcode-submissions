class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            midInd = l + (r - l) // 2
            mid = nums[midInd]
            if mid < target:
                l = midInd + 1
            elif mid > target:
                r = midInd - 1
            else:
                return midInd

        return -1
        