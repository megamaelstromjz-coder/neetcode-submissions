from collections import defaultdict
from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inn = defaultdict(int)
        outt = defaultdict(int)

        for a, b in trust:
            outt[a] += 1
            inn[b] += 1

        for i in range(1, n + 1):
            if inn[i] == n - 1 and outt[i] == 0:
                return i

        return -1