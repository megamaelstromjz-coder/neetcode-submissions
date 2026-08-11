class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        sList = list(s)
        tList = list(t)

        if len(sList) == 0:
            return True
        
        while len(tList) != 0:

            while sList[0] != tList[0]:

                if len(tList) > 1:
                    tList.pop(0)
                else:
                    return False

            tList.pop(0)
            sList.pop(0)
        
            if len(sList) == 0:
                return True

        return False
                
    

