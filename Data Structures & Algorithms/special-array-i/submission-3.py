class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        i = 0
        j = 1

        while j<len(nums):
            
            one = nums[i]
            two = nums[j]

            if one%2 == two%2:
                return False

            i+=1
            j+=1

        return True