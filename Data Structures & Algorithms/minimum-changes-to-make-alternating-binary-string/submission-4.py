class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        for i, ch in enumerate(s):
            # expected char if pattern starts with '0'
            expected = str(i % 2)
            if ch != expected:
                count += 1
        
        return min(count, len(s) - count)