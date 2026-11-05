class Solution(object):
    def minPathSum(self, grid):
        
        m = len(grid)
        n = len(grid[0])

        for j in range(1, n):
            grid[0][j] = grid[0][j] + grid[0][j - 1]

        for i in range(1, m):
            grid[i][0] = grid[i][0] + grid[i - 1][0]


        for i in range(1, m):
            for j in range(1, n):
                
                up = grid[i - 1][j]
                left = grid[i][j - 1]
                
                if up < left:
                    grid[i][j] = grid[i][j] + up
                else:
                    grid[i][j] = grid[i][j] + left

        return grid[m - 1][n - 1]
