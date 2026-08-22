class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count = Counter(list(s))
        setS = set()

        for (k,v) in count.items():
            if v == 1:
                return s.find(k)
        return -1
        
        # l = []

        # for m in setS:
        #     l.append(s.find(m))
        
        # l.sort()

        # if len(l) == 0:
        #     return -1
        # return l[0]
        
        