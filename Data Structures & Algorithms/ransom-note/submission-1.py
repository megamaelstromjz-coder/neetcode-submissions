class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        m = Counter(magazine)
        r = Counter(ransomNote)

        for k,v in r.items():
            if m[k] >= v:
                continue
            else:
                return False
        return True
        