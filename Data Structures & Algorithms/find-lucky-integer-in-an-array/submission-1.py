class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)

        for num in arr[::-1]:
            if count[num] == num:
                return num
            
        return -1