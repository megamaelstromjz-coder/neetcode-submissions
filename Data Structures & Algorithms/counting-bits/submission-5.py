class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = []

        for i in range(n+1):
            num = bin(i)[2:]
            res.append(Counter(num)['1'])

        return res
