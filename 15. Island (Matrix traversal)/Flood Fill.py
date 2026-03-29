class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return []

        r_range = len(image)
        c_range = len(image[0])

        visited = set()

        def dfs(row,col,c):

            visited.add((row,col))
            image[row][col] = color

            directions = [[1,0],[0,1],[-1,0],[0,-1]]

            for i,j in directions:
                new_row = row + i
                new_col = col + j
                if new_row in range(r_range) and new_col in range(c_range) and (new_row,new_col) not in visited and image[new_row][new_col] == c:
                    dfs(new_row,new_col,c)

        dfs(sr,sc,image[sr][sc])

        return image
