class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        count = 0

        while len(s) != 0 and len(g) != 0:
            if g[0] <= s[0]:
                g.pop(0)
                s.pop(0)
                count +=1
            else:
                s.pop(0)
        
        return count
