class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def dfs(n):
            if (n + 1) >= len(nums) - 1:
                return nums[n]
            if n in cache:
                return cache[n]

            money = nums[n]
            moneyNext = 0
            for i in range(n + 2, len(nums)):
                moneyNext = max(moneyNext, dfs(i))
            cache[n] = money + moneyNext

            return cache[n]
        
        if len(nums) > 1:
            return max(dfs(0), dfs(1))
        else:
            return dfs(0)



        