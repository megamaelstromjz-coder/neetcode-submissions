class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        c = Counter(chars)
        for word in words:
            if Counter(word)<=c:
                res+=len(word)

        return res