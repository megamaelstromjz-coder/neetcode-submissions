class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        count = Counter()

        for word in words:
            
            c = Counter(word)

            count = count + c

        print(count)

        
        char = words[0][0]
        no = count[char]

        n = len(words)

        for k,v in count.items():
            if v % n == 0:
                continue
            else:
                return False

        return True
