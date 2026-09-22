class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        mem = [-1] * (n + 1)

        def dp(i):
            if i <= 1:
                return 0
            if mem[i] != -1:
                return mem[i]
            mem[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
            return mem[i]

        return dp(n)