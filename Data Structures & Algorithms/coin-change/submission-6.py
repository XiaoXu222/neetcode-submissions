class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        cache = {}
        
        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            if amount in cache:
                return cache[amount]
            
            choices = []
            for d in coins:
                if dfs(amount - d) >= 0:
                    choices.append(dfs(amount - d))

            if choices:
                cache[amount] = min(choices) + 1
            else:
                cache[amount] = -1
                
            return cache[amount]

        
        return dfs(amount)

            

        