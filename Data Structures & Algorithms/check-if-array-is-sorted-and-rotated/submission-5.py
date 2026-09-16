class Solution:
    def check(self, nums: List[int]) -> bool:
        
        s = sorted(nums)

        for i in range(len(nums)):

            if s == nums:
                return True

            a = s.pop(0)
            s.append(a)
        
        return False