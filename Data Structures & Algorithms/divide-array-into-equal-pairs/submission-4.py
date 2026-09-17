class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        c = Counter(nums)

        # if len(nums) % 2 != 0:
        #     return False
        
        for k,v in c.items():
            if v % 2 != 0:
                return False

        return True
