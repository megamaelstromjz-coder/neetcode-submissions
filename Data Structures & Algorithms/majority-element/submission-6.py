class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)

        for k,v in c.items():
            if len(nums)//2 < v:
                return k