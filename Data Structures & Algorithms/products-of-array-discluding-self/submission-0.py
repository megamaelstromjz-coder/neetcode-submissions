class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        preArr = []
        postArr = []
        output = []

        for i in range(len(nums)):
            if i == 0:
                preArr.append(1)
            else:
                preArr.append(nums[i-1]*preArr[-1])

        nums.reverse()

        for i in range(len(nums)):
            if i == 0:
                postArr.append(1)
            else:
                postArr.append(nums[i-1]*postArr[-1])

        postArr.reverse()

        return [x*y for x,y in zip(preArr,postArr)]

        # 1 2 4 6

        # 1 1 2 8

        # 48 24 6 1