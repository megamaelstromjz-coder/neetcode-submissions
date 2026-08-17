class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        count = 0

        for i in range(len(words)):
            newWords= words[-(len(words)-i-1):]
            for j in range(i + 1, len(words)):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    count += 1
            
        return count
    
    def isPrefixAndSuffix(self, str1, str2):
        len1 = len(str1)
        
        if str2[:len1] == str1 and str2[-len1:] == str1:
            return True
        else:
            return False

        