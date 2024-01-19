class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        
        for i in range(rows -1, -1, -1):
            for j in range(cols -1, -1, -1):
                if i + 1 == rows:
                    continue
                else:
                    minvalue = matrix[i+1][j]
                    if 0 <= j - 1 < cols:
                        minvalue = min(matrix[i+1][j-1], minvalue)
                    if 0 <= j + 1 < cols:
                        minvalue = min(matrix[i+1][j+1], minvalue)
                    matrix[i][j] = minvalue + matrix[i][j]
        return min(matrix[0])
        