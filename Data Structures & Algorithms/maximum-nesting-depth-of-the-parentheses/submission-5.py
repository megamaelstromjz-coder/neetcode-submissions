class Solution:
    def maxDepth(self, s: str) -> int:
        
        stack = []
        lenn = 0
        maxLen = 0

        for i in s:
            if i == '(':
                stack.append(i)
                lenn += 1
                maxLen = max(maxLen, lenn)
            elif i == ')':
                stack.pop()
                lenn-=1

        return max(maxLen, lenn)