class Solution:
    def tribonacci(self, n: int) -> int:

        if n==0:
            return 0
        if n==1:
            return 1
        
        cache = [-1] * (n+1)
        
        cache[0] = 0
        cache[1] = cache[2] = 1

        def dp(i):

            if cache[i] != -1:
                return cache[i]
            
            cache[i] = dp(i-1) + dp(i-2) + dp(i-3)

            return cache[i]
        
        x = dp(n)
        print(cache)
        return x