class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        r_range = len(grid)
        c_range = len(grid[0])

        def dfs(row, col):
            #Here the intuition is to do a simple DFS and track if the node is touching boundary. thats it

            #If out of bounds → not closed
            if row < 0 or col < 0 or row >= r_range or col >= c_range:
                return False
            
            if grid[row][col] == 1 or (row, col) in visited:
                return True

            visited.add((row, col))

            up = dfs(row-1, col)
            down = dfs(row+1, col)
            left = dfs(row, col-1)
            right = dfs(row, col+1)

            return up and down and left and right

        count = 0

        for i in range(r_range):
            for j in range(c_range):
                if grid[i][j] == 0 and (i, j) not in visited:
                    if dfs(i, j):
                        count += 1

        return count
