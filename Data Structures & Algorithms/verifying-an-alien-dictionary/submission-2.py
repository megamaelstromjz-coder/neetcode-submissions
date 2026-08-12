class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {key: number for number, key in enumerate(order)}

        def wordToKey (word):
            return [orderMap[l] for l in word]
        
        for i in range(len(words)-1):
            if wordToKey(words[i]) > wordToKey(words[i+1]):
                return False
        
        return True