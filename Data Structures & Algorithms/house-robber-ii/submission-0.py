class Solution:
    def rob(self, nums: List[int]) -> int:

        m = len(nums)

        if m == 1:
                return nums[0]
        
        def robHouses(houses):

            n = len(houses)
            mem = [-1] * (n) 

            def dp(i):

                if i >= n:
                    return 0 

                if mem[i] != -1:
                    return mem[i]

                mem[i] = max(houses[i] + dp(i+2), dp(i+1))

                return mem[i]

            return dp(0)
        
        return max(robHouses(nums[1:]),robHouses(nums[:-1]))