class Solution:
    def countBits(self, n: int) -> List[int]:
        
        op = []
        for i in range(n+1):
            b = bin(i)[2:]
            c=0
            for i in b:
                if i == '1':
                    c+=1
            op.append(c)
        
        return op