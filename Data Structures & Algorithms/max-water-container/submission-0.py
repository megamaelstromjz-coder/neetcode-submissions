class Solution:
    def maxArea(self, heights: List[int]) -> int:

        n = len(heights)
        maxVol = 0
        i=0
        j=n-1

        while i<j:

            vol = (j-i) * min(heights[i], heights[j])
            maxVol = max(vol,maxVol)

            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        
        return maxVol
            