class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j): 
            # check if we are in range 
            # if the row is less than 0
            # or the row is greater than the amount of rows we have 
            # or columns is less than 0 
            # or the column is greater than the amount of columns we have 
            # or we hit a 0 instead of a 1
            if (i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1'):
                return 
            # if we are in range, change the 1's to 0's
            else:
                grid[i][j] = "0"
                dfs(i, j+1) # right
                dfs(i+1, j) # down 
                dfs(i, j-1) # left
                dfs(i-1, j) # up

        
        num_islands = 0
        for i in range(0, rows): 
            for j in range(0, cols): 
                if grid[i][j] == "1": 
                    # if there is a 1
                    num_islands += 1
                    dfs(i,j)
        
        # time : O(m*n) m is rows, n is columns --> total # of items in grid
        # space: O(m*n)
        return num_islands
