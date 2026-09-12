import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        minusStones = [-n for n in stones]

        heapq.heapify(minusStones)

        while len(minusStones) > 1:
            a = -heapq.heappop(minusStones)
            b = -heapq.heappop(minusStones)

            c = abs(a-b)
            
            if c == 0:
                continue
            else:
                heapq.heappush(minusStones, -c)

        if len(minusStones)==0:
            return 0
        else:
            return -minusStones[0]

                