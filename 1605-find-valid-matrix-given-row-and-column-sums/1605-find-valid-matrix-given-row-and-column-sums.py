class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        
        rows = len(rowSum)
        cols = len(colSum)
        res = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                min_val = min(rowSum[i], colSum[j])
                res[i][j] = min_val
                rowSum[i] -= min_val
                colSum[j] -= min_val
        return res
        