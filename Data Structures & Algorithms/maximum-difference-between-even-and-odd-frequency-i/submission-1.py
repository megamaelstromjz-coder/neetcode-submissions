class Solution:
    def maxDifference(self, s: str) -> int:
        
        count = Counter(list(s))

        a1 = 0
        a2 = 1000

        for (k,v) in count.items():

            if v % 2 == 0:
                a2 = min(a2, v)
        
            else:
                a1 = max(a1, v)
        
        return a1 - a2
        