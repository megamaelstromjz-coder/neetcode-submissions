class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxVal = 0
        n = len(arr)
        op = []
        op.append(-1)

        for i in range(n):
            maxVal = max(maxVal, arr.pop())
            op.append(maxVal)

        op.pop()
        op.reverse()

        return op