class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = [[1]]
        i = 1
        row = [1]

        while i<numRows:
            i+=1
            newrow = [1] * (i)

            for k in range(len(newrow)):
                if k == 0 or k + 1 == len(newrow):
                    continue
                
                newrow[k] = row[k-1] + row[k]

            row = newrow
            print(row)
            res.append(row)


        return res