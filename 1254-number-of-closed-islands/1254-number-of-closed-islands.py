class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        visited = [[False] * cols for _ in range(rows)]
        def backtrack(i, j):
            if i < 0 or i == rows or j < 0 or j == cols:
                return False
            if grid[i][j] == 1:
                return True
            if visited[i][j]:
                return True
            
            visited[i][j] = True
            res1 = backtrack(i + 1, j)
            res2 = backtrack(i - 1, j)
            res3 = backtrack(i, j + 1)
            res4 = backtrack(i, j - 1)
            if res1 and res2 and res3 and res4:
                return True
            return False
        
        res = 0
        
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == 0:
                    if backtrack(i, j):
                        res += 1
                        # print(i, j, res)
        return res
        