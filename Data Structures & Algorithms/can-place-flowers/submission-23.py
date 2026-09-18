class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # if flowerbed == [0] and n == 1:
        #     return True

        
        flowerbed = [0] + flowerbed + [0]
        
        lastEmpty = False 
        c = 0

        for i in range(len(flowerbed)):

            if flowerbed[i] == 1:
                lastEmpty = False
                continue
            
            elif i+1 < len(flowerbed) and flowerbed[i] == 0 and lastEmpty and flowerbed[i+1]!=1:
                c+=1
                lastEmpty = False

            else:
                lastEmpty = True
        
        return c >= n