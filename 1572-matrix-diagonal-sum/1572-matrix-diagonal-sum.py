class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        ans = 0
        for i in range(rows):
            ans += mat[i][i]
        
        for j in range(cols - 1, -1, -1):
            ans += mat[cols - 1 - j][j]
        if rows % 2 == 0:
            return ans
        else:
            return ans - mat[rows//2][cols//2]
        