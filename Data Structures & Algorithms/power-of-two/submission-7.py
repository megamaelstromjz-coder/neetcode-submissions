class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False
        
        x = int(math.log2(n))

        if 2**x == n:
            return True
        return False