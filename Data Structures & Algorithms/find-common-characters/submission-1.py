class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        c = Counter(words[0])

        op = []
        
        for word in words[1:]:

            count = Counter(word)

            c = c & count
        
        print(c)
        
        for k,v in c.items():

            l = v

            while l > 0:
                op.append(k)
                l-=1
        
        return op