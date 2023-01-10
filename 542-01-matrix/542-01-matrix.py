class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        dist = [[10003] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                else:
                    if j - 1 >= 0:
                        dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)
                    if i - 1 >= 0:
                        dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
        
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                else:
                    if j + 1 < cols:
                        dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)
                    if i + 1 < rows:
                        dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
        return dist
                
                
        