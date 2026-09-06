class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return high % 2 if high == low else (high - low) // 2 + 1