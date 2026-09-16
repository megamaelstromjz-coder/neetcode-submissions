class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        maxSum = nums[0]
        subArry = [nums[0]]

        for i in range(1, len(nums)):

            if nums[i-1] < nums[i]:
                subArry.append(nums[i])
            else:
                maxSum = max(maxSum, sum(subArry))
                subArry = [nums[i]]
        
        return max(maxSum, sum(subArry))