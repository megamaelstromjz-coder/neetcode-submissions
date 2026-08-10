class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = dict()

        for index, x in enumerate(nums):
            comp = target - x
            if comp in store:
                return [store[comp], index]
            else:
                store[x] = index
        
        return []