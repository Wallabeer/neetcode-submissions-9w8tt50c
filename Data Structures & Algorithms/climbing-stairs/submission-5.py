class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def helper(i):
            if i in cache:
                return cache[i]
            if i == n:
                return 1
            if i > n:
                return 0
            
            cache[i] = helper(i+1) + helper(i+2)
            return cache[i]
        
        return helper(0)
