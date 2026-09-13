class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        mem = []

        i = 0
        row = [1]
        mem.append(row)

        while i+1 < numRows:

            i+=1

            newRow = [1] * (i+1)

            for j in range(len(newRow)):

                if j == 0 or j+1 == len(newRow):
                    continue
                else:
                    newRow[j] = row[j-1] + row[j]
            
            row = newRow
            mem.append(row)
        
        return mem


