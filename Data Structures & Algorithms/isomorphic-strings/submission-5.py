class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # if len(s) != len(t):
        #     return False
        
        # if s=="abbAB" and t=="ABBAa":
        #     return False
        
        # if s=="H^Gn~abc" and t=="H^Gn~aaa":
        #     return False
        
        # if s == "abc" and t=="cac":
        #     return False


        wordS = list(s)
        wordT = list(t)

        mapST = {}
        mapTS = {}


        for cs,ct in zip(s,t):

            if cs in mapST and mapST[cs] != ct:
                return False
            if ct in mapTS and mapTS[ct] != cs:
                return False
            mapST[cs] = ct
            mapTS[ct] = cs
        
        return True

        