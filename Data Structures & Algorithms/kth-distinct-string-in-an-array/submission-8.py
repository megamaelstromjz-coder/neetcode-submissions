class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res = []
        c = Counter(arr)
        for ch,v in c.items():
            if v == 1:
                res.append(ch)
        
        if len(res) < k:
            return ""
        else:
            return res[k-1]
            