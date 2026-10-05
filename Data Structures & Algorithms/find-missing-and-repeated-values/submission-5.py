class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        res = []
        seen = set()

        for row in grid:
            for c in row:
                if c in seen:
                    res.append(c)
                seen.add(c)
        
        for i in range(1,len(seen)+2):
            if i not in seen:
                res.append(i)

        return res
