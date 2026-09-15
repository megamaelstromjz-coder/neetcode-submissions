class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)

        for k in count:
            if count[k] > len(nums) // 2:
                return k
        
        return -1