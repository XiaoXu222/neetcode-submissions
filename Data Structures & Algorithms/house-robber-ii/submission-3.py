class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i, rob0):
            if i == len(nums) - 1:
                if rob0:
                    return 0
                else:
                    return nums[i]
            if i > len(nums) - 1:
                return 0
            if (i, rob0) in cache:
                return cache[i, rob0]

            right = dfs(i + 1, rob0)

            if i == 0:
                rob0 = True
            left = nums[i] + dfs(i + 2, rob0)
            cache[(i, rob0)] = max(left, right)
            
            return cache[(i, rob0)]

        return dfs(0, False)

            


        