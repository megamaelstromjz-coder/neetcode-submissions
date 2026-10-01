class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        if not s:
            return 0
        
        g.sort()
        s.sort()
        i = 0
        res = 0
        for kid in g:
            while i < len(s) and s[i] < kid:
                i+=1
            if i < len(s):
                res += 1
                i += 1
            else:
                break
        return res