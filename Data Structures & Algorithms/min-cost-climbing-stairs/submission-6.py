class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        mem = [-1]*(n+1)

        def dp(i):

            if i >= n:
                return 0

            if mem[i] != -1:
                return mem[i]

            mem[i] = cost[i] + min(dp(i+1), dp(i+2))

            return mem[i]

        return min(dp(0),dp(1))