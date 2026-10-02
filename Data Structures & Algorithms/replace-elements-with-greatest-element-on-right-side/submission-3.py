class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        i=len(arr)-1
        maxElem = -1
        while i >= 0:
            temp = maxElem
            maxElem = max(maxElem, arr[i])
            arr[i] = temp
            i-=1

        return arr

