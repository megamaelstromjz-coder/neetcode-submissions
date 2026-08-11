class Solution:
    def maxDepth(self, s: str) -> int:
        
        stack = []
        count = 0
        maxCount = 0

        for c in s:
            if c == '(':
                stack.append(c)
                maxCount = max(len(stack), maxCount)
            if c == ')':
                stack.pop()

        return maxCount
        