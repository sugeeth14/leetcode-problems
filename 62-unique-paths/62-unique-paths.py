class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0] * n for _ in range(m)]
        # Initialize the last row with 1 
        for i in range(n):
            res[m-1][i] = 1
        #Initialize the last colums with 1
        for i in range(m):
            res[i][n-1] = 1
        
        # Start filling the grid
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                res[j][i] = res[j][i+1] + res[j+1][i]
        return res[0][0]
        