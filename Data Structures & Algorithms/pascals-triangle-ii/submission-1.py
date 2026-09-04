class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]
        
        c = 1
        mem = [1]

        while c <= rowIndex: 
            c+=1
            row = [1] * c
            for i in range(c):
                if i != 0 and i != c-1:
                    row[i] = mem[i-1] + mem[i]
            
            mem = row
        
        return mem