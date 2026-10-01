class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in setNums:
                new = 1
                for i in range(num + 1, num + len(nums)):
                    if i in setNums:
                        new += 1
                    else:
                        break
                res = max(res, new)
        return res
