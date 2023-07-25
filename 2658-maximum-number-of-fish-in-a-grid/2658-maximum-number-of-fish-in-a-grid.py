class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        
        
        def backtrack(i, j):
            if i < 0 or j < 0 or i == rows or j == cols:
                return 0
            else:
                if grid[i][j] == 0:
                    return 0
                if (i, j) in visited:
                    return 0
                
                visited.add((i, j))
                return grid[i][j] + backtrack(i, j + 1) + backtrack(i, j - 1) + backtrack(i+1, j) + backtrack(i-1,j)
            
            
        res = 0
            
        
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] != 0:
                    current_value = backtrack(i, j)
                    res = max(current_value, res)
        return res
            
        