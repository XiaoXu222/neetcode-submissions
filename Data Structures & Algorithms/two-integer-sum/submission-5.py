class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicies = {}
        for i, n in enumerate(nums):
            indicies[n] = i
        for i, n in enumerate(nums):
            diff = target - n
            if diff in indicies and indicies[diff] != i:
                return [i, indicies[diff]]
        return []

        # diff = []
        # for num in nums:
        #     diff.append(target - num)
        # diff_nodup = set(diff)
        # indices= []
        # for i in range(len(nums)):
        #     if nums[i] in diff_nodup:
        #         indices.append(i)

        # if len(indices) != 2:
        #     indices_clean = []
        #     for index in indices:
        #         if nums[index] != target/2:
        #             indices_clean.append(index) 
        #     return indices_clean
        # else:
        #     return indices


        