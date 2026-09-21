class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        n=len(words)
        
        c = Counter(words.pop(0))


        for word in words:
            local = Counter(word)
            c+=local
        print(c)
        for k,v in c.items():
            if v % n == 0:
                continue
            else:
                return False

        return True