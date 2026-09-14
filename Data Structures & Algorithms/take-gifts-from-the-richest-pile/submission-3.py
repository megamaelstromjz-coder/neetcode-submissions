import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        max_heap = [-n for n in gifts]

        heapq.heapify(max_heap)

        for i in range(k):

            a = -heapq.heappop(max_heap)
            s = int(math.sqrt(a))

            heapq.heappush(max_heap, -s)
            # print(max_heap)

        l = [-n for n in max_heap]
        # print(l)

        return sum(l)

    