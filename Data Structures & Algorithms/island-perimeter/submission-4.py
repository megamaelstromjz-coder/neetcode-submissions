class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        touching = 0
        ones = 0

        for row in grid:
            prev = False
            for c in row:
                if c == 1:
                    if prev:
                        touching+=1
                    prev = True
                    ones+=1
                else:
                    prev = False
        
        i=0
        while i < len(grid[0]):
            prev = False
            for row in grid:
                if row[i] == 1:
                    if prev:
                        touching+=1
                    prev = True
                    ones+=1
                else:
                    prev = False
            i+=1
        
        return 2*ones - 2*touching

                