class Solution:
    def maxDifference(self, s: str) -> int:
        
        maxOdd = 0
        odd = 0

        minEven = 101
        even = 0

        c = Counter(s)

        for k,v in c.items():
            if v % 2 == 0:
                minEven = min(minEven, v)
            else:
                maxOdd = max(maxOdd, v)

        print(maxOdd)
        print(minEven)
        
        return maxOdd - minEven