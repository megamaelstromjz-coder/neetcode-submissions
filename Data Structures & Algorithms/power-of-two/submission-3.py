class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False

        no = math.log2(n)
        if no == int(no):
            return True
        return False