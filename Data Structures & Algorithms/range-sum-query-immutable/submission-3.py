class NumArray:

    def __init__(self, nums: List[int]):
        self.array = nums
        

    def sumRange(self, left: int, right: int) -> int:

        t = 0
        
        s = self.array
        
        for i in range(len(s)):
            if left <= i <= right:
                t+=s[i]
            else:
                continue
        
        return t
            

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)