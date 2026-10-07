class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        c = Counter(arr)
        res = []

        for k,v in c.items():
            if v == k:
                res.append(v)

        if res:
            return sorted(res)[-1]
        return -1