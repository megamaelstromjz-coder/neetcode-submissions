class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        count = 0

        for word in words:
            consistent = True
            for c in word:
                if c in allowed:
                    continue
                consistent = False
            
            count = count + 1 if consistent else count
        
        return count
