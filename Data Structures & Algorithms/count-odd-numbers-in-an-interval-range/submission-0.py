class Solution:
    def countOdds(self, low: int, high: int) -> int:

        def isEven(num):
            if num % 2 == 0: 
                return True
            return False

        diff = high - low

        #if both odd: (diff + 2) /2
        if not isEven(high) and not isEven(low):
            return (diff + 2) // 2
        #if both even, diff / 2
        elif isEven(high) and isEven(low):
            return diff // 2
        # odd - even (diff + 1) / 2
        else:
            return (diff + 1) // 2
