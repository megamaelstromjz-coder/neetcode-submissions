class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        values = [1,5,10,50,100,500,1000]

        mapp = dict(zip(symbols,values))

        valList = list(s)

        total = 0


        valList = [mapp[ch] for ch in s]

        i=0
        while i < len(valList):
            
            if i + 1 < len(valList) and valList[i] < valList[i + 1]:
                total -= valList[i]
            else:
                total += valList[i]
            i+=1




        return total


        # string.append(0)

        # 10 50 1 10