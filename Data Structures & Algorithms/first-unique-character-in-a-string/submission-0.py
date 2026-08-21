class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count = Counter(list(s))

        l = [k for (k,v) in count.items() if v == 1]

        if len(l) == 0:
            return -1

        for i in range(len(list(s))):
            if s[i] in l:
                return i

        return -1