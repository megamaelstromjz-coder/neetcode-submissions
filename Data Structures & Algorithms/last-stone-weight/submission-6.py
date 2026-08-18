
from heapq import heappop, heappush, heapify


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = [-s for s in stones]

        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            s1 = -heapq.heappop(maxHeap)
            s2 = -heapq.heappop(maxHeap)

            if s1 == s2:
                if len(maxHeap) == 0:
                    return 0
                else:
                    continue
            elif s1 > s2:
                heapq.heappush(maxHeap, -(s1 - s2))
            else:
                heapq.heappush(maxHeap, -(s2 - s1))
            
        return -maxHeap[0]




            
        