class Solution:
    def arrangeCoins(self, n: int) -> int:
        
         counter = 1
         rows = 1

         if n == 1:
            return 1

         while counter < n:

            rows += 1
            counter += rows
            

         return rows - 1

         

        