class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        c = Counter(s)

        a = c['1'] - 1
        b = c['0']

        op = ""

        while a > 0:
            op += '1'
            a-=1

        while b > 0:
            op+='0'
            b-=1
        
        return op+'1'