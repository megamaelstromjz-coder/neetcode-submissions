class Solution:
    def check(self, nums: List[int]) -> bool:
        
        comp = sorted(nums)

        for i in range(len(nums)+1):

            a = nums.pop(0)
            nums.append(a)

            if nums == comp:
                return True

        return False