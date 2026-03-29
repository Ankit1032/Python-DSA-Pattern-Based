class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        # Solution 1 - BSF WORKS and MORE INTUITIVE
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


        # Solution 2 - Works and follows the same island code which you write normally
        class Solution:
        def closedIsland(self, grid: List[List[int]]) -> int:
            # BFS
            n_of_islands = 0
            visited = set()
            r_range = len(grid)
            c_range = len(grid[0])
    
            def dfs(row,col):
                #Here the idea is to do simple DFS and check if the nodes are reaching/touching boundary
    
                # if we go out of bounds → not closed
                if row < 0 or col < 0 or row >= r_range or col >= c_range:
                    return False
    
                # water or already visited → doesn't break closed condition
                if grid[row][col] == 1 or (row, col) in visited:
                    return True
                
                visited.add((row,col))
    
                directions = [[-1,0],[1,0],[0,1],[0,-1]]
    
                flag = True  # assume closed
    
                for i,j in directions:
    
                    new_row = row + i
                    new_col = col + j
    
                    # explore all directions (NO boundary restriction)
                    if not dfs(new_row, new_col):
                        flag = False
    
                return flag
    
    
            for i in range(r_range):
                for j in range(c_range):
                    if grid[i][j] == 0 and (i,j) not in visited: #Here 0 means land
                        if dfs(i,j):
                            n_of_islands += 1
    
            return n_of_islands
