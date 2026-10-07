class Solution:
    def climbStairs(self, n: int) -> int:
        
        mem = [-1] * (n+1)

        def dp(i):

            if i == n:
                return 1
            
            if i > n:
                return 0

            if mem[i] != -1:
                return mem[i]

            mem[i] = dp(i+1)+ dp(i+2)

            return mem[i]

        return dp(0)
