class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        
        

        row = [1]
        i=0

        while i<rowIndex:

            i+=1
            newRow = [1] * (i+1)

            for i in range(len(newRow)):
                if i == 0 or i + 1 == len(newRow):
                    continue
                
                newRow[i] = row[i] + row[i-1]
            
            row = newRow

        return row
