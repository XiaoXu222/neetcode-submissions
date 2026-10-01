class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = defaultdict(list)
        for i in range(len(nums)):
            count[nums[i]].append(i)
            nums[i] = target - nums[i]
        for j in range(len(nums)):
            if nums[j] in count:
                for index in count[nums[j]]:
                    if index != j:
                        return [j, index]
            


        