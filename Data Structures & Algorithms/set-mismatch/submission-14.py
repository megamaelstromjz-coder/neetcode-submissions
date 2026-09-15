class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        c = Counter(nums)
        a = -1
        b = -1
        

        for i in range(1, len(nums)+1):
            if c[i] == 2:
                a = i

            if c[i] == 0:
                b = i 

        if a == -1:
            a = 1
        
        if b == -1:
            b = len(nums)

        return [a,b]           