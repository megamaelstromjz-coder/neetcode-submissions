class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)

        largest = 0

        for (k,v) in count.items():
            if v == k:
                largest = max(largest, k)
            
        if largest == 0:
            return -1
        return largest
