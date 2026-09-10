class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set(allowed)
        c=0
        for word in words:
            for i in range(len(word)):
                if word[i] not in s:
                    break
                else:
                    if i + 1 == len(word):
                        c+=1
        
        return c
            