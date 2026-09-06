class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        count = Counter(arr)

        op = []

        for char,v in count.items():
            if v == 1:
                op.append(char)

        if len(op) < k:
            return ""
        
        else:
        
            return op[k-1]

