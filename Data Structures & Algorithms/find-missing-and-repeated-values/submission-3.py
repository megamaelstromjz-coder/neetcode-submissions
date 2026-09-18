class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        l = []
        n = len(grid)
        seen = set()
        a=-1

        for row in grid:
            for i in row:
                if i in seen:
                    a = i
                seen.add(i)
                l.append(i)

        for i in range(1, n*n+1):
            if i not in seen:
                return [a,i]
