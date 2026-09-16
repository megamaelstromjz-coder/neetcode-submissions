class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        i = 0
        j = len(nums)-1

        while i<=j:
            mid = i + (j-i)//2

            if nums[mid] < target:
                i = 1 + mid
            
            elif nums[mid] > target:
                j = mid - 1
            
            else:
                return mid
        
        return -1