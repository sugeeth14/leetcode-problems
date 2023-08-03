class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        
        dic = {}
        rows = len(matrix)
        cols = len(matrix[0])
        def backtrack(i, j):
            
            if (i,j) in dic:
                return dic[(i, j)]
            
            res = 1
            res1, res2, res3, res4 = 0, 0, 0, 0
            if i - 1 >= 0 and matrix[i-1][j] > matrix[i][j]:
                res1 = backtrack(i-1, j)
            if j - 1 >=0 and matrix[i][j-1] > matrix[i][j]:
                res2 = backtrack(i, j - 1)
            
            if i + 1 < rows and matrix[i+1][j] > matrix[i][j]:
                res3 = backtrack(i + 1, j)
                
            if j + 1 < cols and matrix[i][j + 1] > matrix[i][j]:
                res4 = backtrack(i, j + 1)
                
            res = max(res1, res2, res3, res4) + res
            
            
            
            dic[(i, j)] = res
            
            return res
        
        ans = 1
        
        for i in range(rows):
            for j in range(cols):
                backtrack(i, j)
                ans = max(ans, dic[(i, j)])
        # print(dic)
        return ans
        
        
        