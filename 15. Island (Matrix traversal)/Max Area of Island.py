class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        max_area = float('-inf')
        visited = set()
        r_range = len(grid)
        c_range = len(grid[0])
        

        def dfs(row,col):
            nonlocal area

            visited.add((row,col))
            area += 1

            direction = [[1,0],[0,1],[-1,0],[0,-1]]

            for i,j in direction:
                new_row = row + i
                new_col = col + j

                if new_row in range(0,r_range) and new_col in range(0,c_range) and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                    # area += 1 : I was adding area here but this meant i only added area when visiting neighbours which 
                    dfs(new_row,new_col)

        area: int

        for i in range(r_range):
            for j in range(c_range):
                if grid[i][j] == 1 and (i,j) not in visited:
                    area = 0
                    dfs(i,j)
                    max_area = max(max_area, area)

        return 0 if max_area == float(-inf) else max_area #0 is when max_area will never get updated


