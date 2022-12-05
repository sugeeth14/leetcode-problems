class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        dp = [[rows + cols + 1] * cols for _ in range(rows)]
        
        visit = set()
        
        
        def backtrack(i, j, depth):
            if i < 0 or j < 0 or i == rows or j == cols:
                return
            if (i, j) in visit:
                return
            
            if grid[i][j] == 1:
                return
            else:
                visit.add((i, j))
                if depth < dp[i][j]:
                    dp[i][j] = depth
                    backtrack(i+1, j, depth + 1)
                    backtrack(i-1, j, depth + 1)
                    backtrack(i, j + 1, depth + 1)
                    backtrack(i, j - 1, depth + 1)
                visit.remove((i, j))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                    backtrack(i + 1, j, 1)
                    backtrack(i - 1, j, 1)
                    backtrack(i, j + 1, 1)
                    backtrack(i, j - 1, 1)
        # print(dp)
        res = -1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    res = max(res, dp[i][j])
        return res if res!= rows + cols + 1 else -1
            
                
                
        
        
        