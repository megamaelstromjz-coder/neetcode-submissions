class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxConsec = 0
        counter = 0
        prevOne = False

        for i in range(len(nums)):
            
            if nums[i] == 0:
                maxConsec = max(maxConsec,counter)
                counter = 0
                prevOne = False
            
            elif nums[i] == 1 and prevOne == False:
                counter = 1
                prevOne = True

            elif nums[i] == 1 and prevOne == True:
                counter += 1

        return max(counter, maxConsec)
