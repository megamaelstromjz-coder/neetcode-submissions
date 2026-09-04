class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        arr = [num**2 for num in nums]

        return sorted(arr)