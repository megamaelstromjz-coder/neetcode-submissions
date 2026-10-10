class Solution:
    def tribonacci(self, n: int) -> int:
        

        mem = [-1] * (n+1)


        def dp(i):

            if i == 0:
                return 0

            if i == 1 or i == 2:
                return 1
            
            if mem[i] != -1:
                return mem[i]

            mem[i] = dp(i-1) + dp(i-2) + dp(i-3)

            return mem[i]

        
        return dp(n)