class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        for i in range(len(nums)-1):

            first = nums[i] % 2
            second = (nums[i+1]) % 2

            if first == second:
                return False
        
        return True