class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # dp = [0] * (n+1)
        cache = {}
        cache[0] = 0
        cache[1] = 0
        for i in range(2, n+1):
            # print(i, i-2, i-1)
            # print(min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1]))
            # dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
            cache[i] = min(cache[i-2]+cost[i-2], cache[i-1]+cost[i-1])
        return cache[n]
        
