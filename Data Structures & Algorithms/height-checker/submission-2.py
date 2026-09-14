class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        expected = sorted(heights)

        pairs = zip(expected, heights)

        c = 0

        for a,b in pairs:
            if a!=b:
                c+=1

        return c