class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numSet = set()
        numList = list(nums)
        duplicate = 0
        missing = 0

        for num in nums:
            if num not in numSet:
                numSet.add(num)
            else:
                duplicate = num

        l = sorted(numList)
        s = sorted(list(numSet))

        for i in range(len(s)):
            if i+1 != s[i]:
                missing = i+1
                break

        if missing != 0:
            return [duplicate, missing]
        else:
            return [duplicate, len(s)+1]

        # s: 1
        # i: 1
        
        # 1 2 3 4 6 7 8 9 9: l
        # 1 2 3 4 5 6 7 8 9: i

        # 1 2 3 4 5 6 7 8 9: s
        # 1 2 3 4 5 6 7 8 9 10: i

