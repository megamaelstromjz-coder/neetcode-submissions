class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:


        nums.sort()

        minRes = nums[k-1] - nums[0]

        for i in range(k,len(nums)):

            res = nums[i] - nums[i-k+1]
            minRes = min(minRes, res)

        return minRes
            
