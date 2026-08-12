class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashmap = set()
        # for num in nums:
        #     if num in hashmap:
        #         return True
        #     hashmap.add(num)
        # return False

        array2set = set(nums)
        if len(nums) != len(array2set):
            return True
        else:
            return False
        