class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        res = []
        
        for word in words:
            test = False
            for w in words:
                if w == word:
                    continue
                elif word in w:
                    test = True
            
            if test:
                res.append(word)

        return res
