class Solution:
    def hammingWeight(self, n: int) -> int:
        
        b = bin(n)[2:]
        print(b)
        c=0
        for i in range(len(b)):
            if b[i] == '1':
                c+=1
        return c
