class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        # value -> out
        # key -> in
        count = Counter() 


        for person, tru in trust:

            count[person] -= 1
            count[tru] += 1

        for k in range(1, n+1):
            
            if count[k] == n-1:
                return k
        
        return -1


