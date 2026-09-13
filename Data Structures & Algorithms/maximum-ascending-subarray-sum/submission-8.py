class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        summy = 0
        maxSum = 0

        for i in range(0, len(nums)):

            if i == 0:
                summy += nums[i]

            elif nums[i-1] < nums[i]:
                summy += nums[i]
            
            else:
                maxSum = max(maxSum, summy)
                summy = nums[i]
        
        return max(maxSum, summy)
