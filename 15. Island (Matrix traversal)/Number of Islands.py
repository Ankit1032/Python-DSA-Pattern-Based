class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS
        # if not grid:
        #     return 0

        # number_of_islands = 0
        # row_length = len(grid)
        # col_length = len(grid[0])
        # visited = set()

        # def bfs(row,col):
            
        #     Q = deque()
        #     visited.add((row,col))
        #     Q.append((row,col))

        #     while Q:
        #         row, col = Q.popleft()

        #         directions = [ [0,1],[0,-1],[-1,0],[1,0] ]

        #         for r,c in directions:
        #             new_r = row + r
        #             new_c = col + c
        #             if new_r in range(row_length) and new_c in range(col_length) and grid[new_r][new_c] == "1" and (new_r, new_c) not in visited:
        #                 Q.append((new_r, new_c))
        #                 visited.add((new_r, new_c))

        # for r in range(row_length):
        #     for c in range(col_length):
        #         if grid[r][c] == "1" and (r,c) not in visited:
        #             bfs(r,c)
        #             number_of_islands = number_of_islands+1

        # return number_of_islands
        
        # DFS - Even tho it gets solved with both BFS and DFS, DFS felt more intuitive
        n_of_islands = 0
        visited = set()
        r_range = len(grid)
        c_range = len(grid[0])

        def dfs(row,col):
            
            visited.add((row,col))

            directions = [[-1,0],[1,0],[0,1],[0,-1]]

            for i,j in directions:

                '''
                Earlier I was trying
                row = row + i
                col = col + j
                Which is wrong because if row gets updated in 1st iterate, 2nd iteration will add onto ti again which is not the same base value of row and col
                '''

                new_row = row + i
                new_col = col + j

                if new_row in range(0,r_range) and new_col in range(0,c_range) and grid[new_row][new_col] == "1" and (new_row,new_col) not in visited:
                    dfs(new_row, new_col)


        for i in range(r_range):
            for j in range(c_range):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    n_of_islands += 1

        return n_of_islands
