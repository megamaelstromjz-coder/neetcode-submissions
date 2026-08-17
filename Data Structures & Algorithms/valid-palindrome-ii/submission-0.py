class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        if s[::-1] == list(s):
            return True
        
        for i in range(len(s)):
            tbPopped = list(s).copy()
            tbPopped.pop(i)

            if tbPopped == tbPopped[::-1]:
                return True
            
        return False