class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        sorted_words = sorted(words, key=len) 

        op = set()

        for word in words:
            for w in words:
                if word in w and w != word:
                    op.add(word)

        return list(op)