class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        # odd = half then floor: 3 -> 1; 5 -> 2
        # even = half then -1: 4 -> 1; 6 -> 2; 8 -> 3

        flowerbed = [0] + flowerbed + [0]

        counterZ = -1
        store = []

        for i in range(len(flowerbed)):

            if flowerbed[i] == 1:
                if counterZ != -1: #its seen a new string of 0's
                    store.append(counterZ)
                    counterZ = -1

            else:
                if counterZ == -1:
                    counterZ = 1
                else:
                    counterZ += 1

            if i == len(flowerbed) - 1 and counterZ > -1:
                store.append(counterZ)
        
        for i in range(len(store)):
            
            if store[i] % 2 == 0:
                store[i] = store[i] // 2 - 1
            else:
                store[i] = store[i] // 2 

        if sum(store) >= n:
            return True
        else:
            return False
            
