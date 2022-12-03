class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        rows = len(grid)
        cols = len(grid[0])
        
        visited = [[False] * cols for _ in range(rows)]
        
        def backtrack(i, j):
            if i < 0 or i == rows or j < 0 or j == cols or visited[i][j] or grid[i][j] == 0:
                return 0
            else:
                count = 1
                visited[i][j] = True
                count = count + backtrack(i + 1, j) + backtrack(i - 1, j) + backtrack(i, j + 1) + backtrack(i, j - 1)
                return count
            
        max_res = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    island_size = backtrack(i, j)
                    max_res = max(max_res, island_size)
        return max_res
                
            
            
            
        