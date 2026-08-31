class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
     
        a = -1
        b = -1

        newList = [item for sublist in grid for item in sublist]
        newList.sort()

        standard = list(range(1, len(grid[0]) ** 2  ))

        count = Counter(newList)

        for (k,v) in count.items():
            if v == 2:
                a = k

        newNew = newList
        newNew.pop(newList.index(a))

        print(newList)
        print(standard)


        zippy = list(zip(standard, newNew))

        print(zippy)

        for (k,v) in zippy:
            if k != v:
                b = k
                print(b)
                break
        
        if b == -1:
            b = standard[-1] + 1
        
        return [a,b]
            
            

        