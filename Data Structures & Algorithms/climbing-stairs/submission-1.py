class Solution:
    def climbStairs(self, n: int) -> int:
        
        mem = [-1] * (n+1)

        if n==1:
            return 1
        if n==2:
            return 2

        def dp(i):

            if i == 1:
                return 1
            if i == 2:
                return 2
            
            if mem[i] != -1:
                return mem[i]
            
            mem[i] = dp(i-1) + dp(i-2)

            return mem[i]

        
        return dp(n)