class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        idx = -1

        for i in range(len(nums)):
            if i>0 and nums[i-1] < target < nums[i]:
                return i
            elif nums[i] == target:
                return i
            elif nums[len(nums)-1] < target:
                return len(nums)
            elif len(nums) > 0 and nums[0] > target:
                return 0
                
            
        return idx