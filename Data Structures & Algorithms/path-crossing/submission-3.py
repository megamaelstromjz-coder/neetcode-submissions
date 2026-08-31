class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        x = 0
        y = 0

        pos = {(0,0)}

        for direction in path:

            if direction == "N":
                x += 1
            elif direction == "S":
                x -= 1
            elif direction == "E":
                y += 1
            elif direction == "W":
                y -= 1
            
            if (x,y) not in pos:
                pos.add((x,y))
            else:
                return True
            
        print(pos)
        
        return False
            

