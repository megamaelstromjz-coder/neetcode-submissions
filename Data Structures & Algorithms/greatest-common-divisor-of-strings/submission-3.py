class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        maxLen = ""

        if str1 == str2:
            return str1

        if len(str1) < len(str2):
            smaller = str1
            larger = str2
        else: 
            smaller = str2
            larger = str1

        
        n = len(smaller)
        factors = [i for i in range(1, n + 1) if n % i == 0]

        for i in range(len(factors)):
            temp = smaller[0:factors[i]]
            if temp in larger and len(temp) > len(maxLen):
                
                if len(temp) <= 0.5 * len(larger) and temp+temp in larger:
                    maxLen = temp
                    

        
        return maxLen
            