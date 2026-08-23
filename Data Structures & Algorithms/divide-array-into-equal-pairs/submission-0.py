class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()

        while len(nums) > 0:
            if nums[0] == nums[1]:
                nums.pop(0)
                nums.pop(0)
            else:
                return False
            
        return True