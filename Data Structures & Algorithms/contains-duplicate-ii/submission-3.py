class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen = {}

        for i in range(len(nums)):
            n = nums[i]

            if n in seen and abs(seen[n]-i)<=k:
                return True
            seen[n] = i

        return False
            
            