class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = []

        for word in words:
            wordList = list(words)
            wordList.remove(word)

            for i in range(len(wordList)):
                
                if word in wordList[i] and word not in output:
                    output.append(word)

        return output