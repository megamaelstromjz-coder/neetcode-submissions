class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        cache = [-1] * (n + 1)

        def dp(i):
            if i <= 1:
                return 0
            
            if cache[i] != -1:
                return cache[i]
            
            cache[i] = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])

            return cache[i]
        
        return dp(n)
