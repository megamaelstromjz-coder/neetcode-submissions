class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        
        # If the color is already the target color, no changes are needed
        if original_color == color:
            return image
        
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            # If the current pixel matches the original color, update it and check neighbors
            if image[r][c] == original_color:
                image[r][c] = color
                
                # Move Up
                if r > 0: 
                    dfs(r - 1, c)
                # Move Down
                if r + 1 < rows: 
                    dfs(r + 1, c)
                # Move Left
                if c > 0: 
                    dfs(r, c - 1)
                # Move Right
                if c + 1 < cols: 
                    dfs(r, c + 1)
        
        dfs(sr, sc)
        return image
