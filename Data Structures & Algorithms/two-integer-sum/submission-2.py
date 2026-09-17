class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}

        a = -1
        b = -1

        for i,v in enumerate(nums):

            comp = target - v
            if comp in d:
                a = d[comp]
                b = i
                break
            else:
                d[v] = i

        return [a,b]
                
