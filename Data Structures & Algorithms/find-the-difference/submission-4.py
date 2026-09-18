class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        ss = Counter(s)
        tt = Counter(t)

        for k,v in tt.items():
            if ss[k] < v:
                return k
        

