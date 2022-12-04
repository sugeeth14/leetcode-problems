class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        visited = [[False] * cols for _ in range(rows)]

        
        
        def backtrack(i, j):
            if visited[i][j]:
                return
            else:
                visited[i][j] = True
                if i - 1 >= 0 and heights[i-1][j] >= heights[i][j]:
                    backtrack(i - 1, j)
                if i + 1 < rows and heights[i + 1][j] >= heights[i][j]:
                    backtrack(i + 1, j)
                if j - 1 >= 0 and heights[i][j-1] >= heights[i][j]:
                    backtrack(i, j - 1)
                if j + 1 < cols and heights[i][j + 1] >= heights[i][j]:
                    backtrack(i , j + 1)
        
        for i in range(rows):
            backtrack(i, 0)
        for j in range(cols):
            backtrack(0, j)
        # print(visited)
        visited2 = [[False] * cols for _ in range(rows)]
        def backtrack2(i, j):
            if visited2[i][j]:
                return
            else:
                visited2[i][j] = True
                if i - 1 >= 0 and heights[i-1][j] >= heights[i][j]:
                    backtrack2(i - 1, j)
                if i + 1 < rows and heights[i + 1][j] >= heights[i][j]:
                    backtrack2(i + 1, j)
                if j - 1 >= 0 and heights[i][j-1] >= heights[i][j]:
                    backtrack2(i, j - 1)
                if j + 1 < cols and heights[i][j + 1] >= heights[i][j]:
                    backtrack2(i , j + 1)
        
        for i in range(rows):
            backtrack2(i, cols - 1)
        for j in range(cols):
            backtrack2(rows - 1, j)
        res = []
        for i in range(rows):
            for j in range(cols):
                if visited[i][j] and visited2[i][j]:
                    res.append([i, j])
        return res
        
        
                
        