class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMAPt = {}
        tMAPs = {}

        for char_s, char_t in zip(s, t):
            # Check if char_s is already mapped to a different char in t
            if char_s in sMAPt and sMAPt[char_s] != char_t:
                return False

            # Check if char_t is already mapped to a different char in s
            if char_t in tMAPs and tMAPs[char_t] != char_s:
                return False

            sMAPt[char_s] = char_t
            tMAPs[char_t] = char_s

        return True