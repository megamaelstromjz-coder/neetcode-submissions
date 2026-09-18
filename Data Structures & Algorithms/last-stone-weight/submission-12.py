class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort(reverse=True)
            a = stones.pop(0)
            b = stones.pop(0)

            if a == b:
                continue
            else:
                stones.append(abs(a-b))
        
        if len(stones) == 1:
            return stones[0]
        else:
            return 0