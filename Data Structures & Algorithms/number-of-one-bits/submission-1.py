class Solution:
    def hammingWeight(self, n: int) -> int:
        l = [int(s) for s in str(bin(n)[2:])]
        count = Counter(l)

        return count[1]