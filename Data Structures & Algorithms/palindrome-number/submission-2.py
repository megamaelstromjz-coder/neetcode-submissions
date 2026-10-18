class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return list(x) == list(x)[::-1]