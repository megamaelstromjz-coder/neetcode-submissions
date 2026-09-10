class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        if len(nums) % 2 !=0:
            return False
        
        nums.sort()

        for i in range(len(nums)//2):
            a = nums.pop()
            b = nums.pop()

            if a!=b:
                return False

        return True

