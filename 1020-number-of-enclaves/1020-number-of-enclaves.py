class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        visited = [[False] * cols for _ in range(rows)]
        
        def backtrack(i, j, count):
            if i < 0 or i == rows or j < 0 or j == cols:
                count = 0
                return count
            if visited[i][j]:
                return count
            if grid[i][j] == 0:
                return count
            visited[i][j] = True
            count += 1
            count1 = backtrack(i + 1, j, count)
            count2 = backtrack(i-1, j, count)
            count3 = backtrack(i, j + 1, count)
            count4 = backtrack(i, j - 1, count)
            if count1 == 0 or count2 == 0 or count3 == 0 or count4 == 0:
                return 0
            else:
                return count1 + count2 + count3 + count4 - 3*count
                
        res = 0
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == 1:
                    res += backtrack(i, j, 0)
        return res
        