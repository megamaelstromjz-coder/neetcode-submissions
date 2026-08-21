class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        i=0
        maxBs = 0

        while i+k <= len(blocks):
            
            counter= 0
            for letter in list(blocks[i:i+k]):
                if letter == "B":
                    counter+=1
            maxBs = max(maxBs, counter)
            i+=1
        
        return k - maxBs