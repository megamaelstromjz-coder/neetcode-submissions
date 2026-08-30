class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        mem = [-1] * (n) 

        def dp(i):

            if i >= n:
                return 0 

            if mem[i] != -1:
                return mem[i]

            mem[i] = max(nums[i] + dp(i+2), dp(i+1))

            return mem[i]

        return dp(0)
        