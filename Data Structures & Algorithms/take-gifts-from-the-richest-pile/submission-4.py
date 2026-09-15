import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        maxHeap = [-n for n in gifts]

        heapq.heapify(maxHeap)

        for i in range(k):
            a = -heapq.heappop(maxHeap)
            b = int(math.sqrt(a))

            heapq.heappush(maxHeap, -b)

        
        return -sum(maxHeap)
