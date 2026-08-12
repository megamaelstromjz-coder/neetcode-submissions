class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        op = [0, 0]

        count = Counter(nums)

        for i in range(1, len(nums)+1):
            if count[i] == 0:
                op[1] = i
            if count[i] == 2:
                op[0] = i
        
        return op