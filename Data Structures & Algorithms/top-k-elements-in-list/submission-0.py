from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        tuples = counter.items()
        sortedTuples = heapq.nlargest(k, tuples, key = lambda x: x[1])
        final = [item[0] for item in sortedTuples]
        return final
    