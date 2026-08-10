class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        pixColour = image[sr][sc]

        if pixColour == color:
            return image
                    
        def paint (row, col):

            image[row][col] = color

            if row+1 < rows and image[row+1][col] == pixColour:
                paint(row+1, col)
            if row-1>=0 and image[row-1][col] == pixColour:
                paint(row-1,col)
            if col+1 < cols and image[row][col+1] == pixColour:
                paint(row,col+1)
            if col-1>= 0 and image[row][col-1] == pixColour:
                paint(row,col-1)

        paint(sr,sc)

        return image
        