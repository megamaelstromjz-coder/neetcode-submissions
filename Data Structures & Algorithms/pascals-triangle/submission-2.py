class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        op = [[1]]

        i = 0
        row = [1]

        while i < numRows-1:

            i+=1

            newRow = [1] * (i+1)

            for j in range(len(newRow)):
                
                if j == 0 or j == len(newRow)-1:
                    continue
                else:
                    newRow[j] = row[j-1] + row[j]

            row = newRow
            op.append(row)
        
        return op