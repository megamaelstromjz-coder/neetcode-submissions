class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        output = []
        n = len(numbers)
        i = 0
        j = n-1

        while i < j:
            n1 = numbers[i]
            n2 = numbers[j]
            
            if n1 + n2 < target:
                i+=1
            elif n1 + n2 > target:
                j-=1
            else:
                break
        
        return [i+1,j+1]

            

