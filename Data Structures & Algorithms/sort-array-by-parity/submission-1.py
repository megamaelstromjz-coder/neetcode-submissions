class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        e = []
        o = []

        for num in nums:
            if num % 2 == 0:
                e.append(num)
            else:  
                o.append(num)

        return e + o
