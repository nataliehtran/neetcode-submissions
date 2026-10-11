class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 1 --> land 
        # 0 --> water 

        best = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j): 
            # replace 1 with 0
            # count how many 1's we are replacing 
            # if that value is larger than max, replace max with it
            # recursively call dfs (in each valid direction)
            if (i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != 1): 
                return
            else:
                grid[i][j] = 0
                nonlocal count
                count += 1
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i - 1, j)
                dfs(i, j + 1)

        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j] == 1: 
                    # land 
                    # resetting count 
                    count = 0
                    dfs(i, j)
                    # for each island (before we sink it)
                    # check if the amount of land it has is greater than the best island previously set 
                    best = max(best, count)

        # return best 
        return best