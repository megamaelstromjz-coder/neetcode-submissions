class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 100
                c+=1
        
        nums.sort()
        print(nums)
        return len(nums) - c