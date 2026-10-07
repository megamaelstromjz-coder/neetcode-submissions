class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n<=0:
            return False
        
        x = int(math.log2(n))

        return 2**x == n