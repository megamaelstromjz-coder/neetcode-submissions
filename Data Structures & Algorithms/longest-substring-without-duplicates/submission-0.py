class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0
        
        if s == "":
            return 0

        if len(Counter(s)) == 1:
            return 1

        count = Counter()
        l = 0

        for r in range(len(s)):
            count[s[r]] += 1             

            while count[s[r]] != 1:
                count[s[l]] -= 1
                l+=1
            
            res = max(res, r - l + 1)

        return res
            



        