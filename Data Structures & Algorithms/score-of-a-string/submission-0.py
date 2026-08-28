class Solution:
    def scoreOfString(self, s: str) -> int:

        t = 0
        
        for i in range(len(s)):
            if i > 0:
                l1 = ord(s[i-1])
                l2 = ord(s[i])
                t += abs(l1 - l2)
        
        return t
