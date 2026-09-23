class Solution:
    def climbStairs(self, n: int) -> int:

        def mem(n, cache):
            if n < 0:
                return 0
            if n == 0:
                return 1
            if n in cache:
                return cache[n]

            cache[n] = mem(n - 1, cache) + mem(n - 2, cache)
            return cache[n]
        
        return mem(n, {})
            
        