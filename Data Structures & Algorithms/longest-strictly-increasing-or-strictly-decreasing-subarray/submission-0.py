class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        maxValD = 1
        maxValU = 1

        chainU = 1
        chainD = 1

        for i in range(len(nums)):

            if i + 1 < len(nums) and nums[i] < nums[i+1]:
                chainU+=1
                maxValD = max(chainD,maxValD)
                chainD = 1

            if i + 1 < len(nums) and nums[i] > nums[i+1]:
                chainD+=1
                maxValU = max(chainU,maxValU)
                chainU = 1

            if i + 1 < len(nums) and nums[i] == nums[i+1]:
                chainD = 1
                chainU = 1

            maxValU = max(chainU,maxValU)
            maxValD = max(chainD,maxValD)


        return max(maxValU,maxValD)