class Solution:
    def countBits(self, n: int) -> List[int]:

        def one(num):
            b = bin(num)[2:]
            c = 0

            for i in b:
                if i == '1':
                    c+=1
            return c

        op = []

        for i in range(n+1):
            op.append(one(i))
        
        return op