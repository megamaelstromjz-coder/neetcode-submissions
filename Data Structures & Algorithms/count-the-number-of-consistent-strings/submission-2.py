class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        count = 0

        for word in words:
            approve = True
            for c in word:
                if c not in allowed:
                    approve = False
            if approve:
                count+=1
            
        
        return count
