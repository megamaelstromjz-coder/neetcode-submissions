class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        s = set(nums)
        op = []

        for i in range(1,len(nums)+1):

            if i not in s:
                op.append(i)
        
        return op
                
        

