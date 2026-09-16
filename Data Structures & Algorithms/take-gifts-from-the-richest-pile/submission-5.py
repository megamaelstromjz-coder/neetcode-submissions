from _heapq import heappush
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        maxHeap = [-n for n in gifts]

        heapq.heapify(maxHeap)

        for i in range(k):
            
            a = -heapq.heappop(maxHeap)

            a = int(math.sqrt(a))

            heapq.heappush(maxHeap, -a)

        return -sum(maxHeap)