class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort()
        pref = strs[0]

        for s in strs:

            while not s.startswith(pref):
                pref = pref[:-1]
        
        return pref