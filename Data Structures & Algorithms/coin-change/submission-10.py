class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        
        def dfs(amount):
            if amount == 0:
                return 0
            # if amount < 0:
            #     return -1
            if amount in cache:
                return cache[amount]
            
            res = 1e9
            choices = []
            for d in coins:
                if amount - d >= 0:
                    res = min(res, 1 + dfs(amount - d))

            cache[amount] = res

            return res

        if dfs(amount) >= 1e9:
            return -1
        else:
            return dfs(amount)

            

        