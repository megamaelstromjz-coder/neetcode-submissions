class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ones= 0
        touching = 0

        for row in grid:
            for i in range(len(row)):
                
                if i == 0:
                    ones = ones + 1 if row[i] == 1 else ones
                elif row[i-1] == row[i] == 1:
                    ones+=1
                    touching+=1
                elif row[i] == 1:
                    ones+=1

        
        
        for i in range(len(grid[0])):
            
            prevOne = False
            for row in grid:
                if row[i] == 1:
                    if prevOne:
                        touching += 1
                    prevOne = True
                else:
                    prevOne = False
                


        
        print(ones)
        print(touching)

        return 4*ones -  2* touching
