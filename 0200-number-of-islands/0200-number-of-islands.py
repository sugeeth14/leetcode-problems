class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Algorithm:
        1. Iterate over the rows and columns column by column and then row by row
        2. For each item, if the value of grid is 1, add 1 to the res
        3. If it is 1, then call the back track function
        4. In the backtrack function write recursive function to make the neighbors continously 0
        5. Return once there are no neighbors.
        6. Return res at the end.
        '''
        
        rows = len(grid)
        cols = len(grid[0])
        
        def backtrack(i, j):
            if i < 0 or i == rows or j < 0 or j == cols:
                return
            if grid[i][j] == "0":
                return
            else:
                grid[i][j] = "0"
                # visit all  the neighbors
                backtrack(i + 1, j)
                backtrack(i-1, j)
                backtrack(i, j + 1)
                backtrack(i, j - 1)
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    res += 1
                    backtrack(i, j)
        return res