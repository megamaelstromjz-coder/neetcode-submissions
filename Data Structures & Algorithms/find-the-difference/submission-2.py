class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        sString = list(sorted(s))
        tString = list(sorted(t))

        for i in range(min(len(s), len(t))):

            if sString[i] == tString[i]:
                continue
            else:
                return tString[i]
        
        return tString[-1]