class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def subsets(a):
            for r in range(len(a)+1):
                yield from combinations(a,r)
        
        subsetS = subsets(nums)

        op = 0

        for listt in subsetS:
            local = 0
            for i in listt:
                local^=i
            op+=local

        return op