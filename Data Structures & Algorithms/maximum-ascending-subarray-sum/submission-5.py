class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        curr = 0
        maxSum = 0

        for i in range(len(nums)):

            if i == 0:
                curr = nums[i]
            elif nums[i-1] < nums[i]:
                curr+=nums[i]
            else:
                maxSum = max(curr, maxSum)
                curr = nums[i]
        

       
        
        return max(curr, maxSum)
