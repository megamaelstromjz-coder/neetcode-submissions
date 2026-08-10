class NumArray:

    def __init__(self, nums: List[int]):
        self.intList = nums

    def sumRange(self, left: int, right: int) -> int:
        total = 0
        newList = self.intList[left:(right+1)]
        diff = right - left + 1
        for i in range(diff):
           total += newList[i] 
        return total
            


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)