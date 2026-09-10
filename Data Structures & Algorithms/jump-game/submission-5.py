class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 1
        # res = True
        # while i > 0:
        for j in range(i - 1, -1, -1):
            if j + nums[j] >= i:
                i = j
        return i == 0
        #     if i != j:
        #         res = False
        #         break
        # return res


        