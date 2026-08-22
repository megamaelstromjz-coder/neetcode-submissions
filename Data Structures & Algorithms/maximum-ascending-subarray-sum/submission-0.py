class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        maxA = nums[0]
        curr = nums[0]

        for i in range(1,len(nums)):
            curr = curr + nums[i] if nums[i-1] < nums[i] else nums[i]
            maxA = max(curr, maxA)
        return maxA
            
