class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        queue = collections.deque()
        rows = len(heights)
        cols = len(heights[0])
        
        res = [[float("inf")] * cols for _ in range(rows)]
        
        present_dict = {}
        for i in range(rows):
            for j in range(cols):
                present_dict[(i, j)] = False
        queue.append((0,0))
        present_dict[(0,0)] = True
        res[0][0] = 0
        while queue:
            top = queue.popleft()
            i, j = top[0], top[1]
            if i + 1 < rows:
                current = max(res[i][j], abs(heights[i][j] - heights[i+1][j]))
                if current < res[i+1][j]:
                    # update the result and add into queue if not present
                    res[i+1][j] = current
                    if present_dict[(i+1,j)] == False:
                        present_dict[(i+1,j)] = True
                        queue.append((i+1,j))
            if i - 1 >= 0:
                current = max(res[i][j], abs(heights[i][j] - heights[i-1][j]))
                if current < res[i-1][j]:
                    # update the result and add into queue if not present
                    res[i-1][j] = current
                    if present_dict[(i-1,j)] == False:
                        present_dict[(i-1,j)] = True
                        queue.append((i-1,j))
            
            if j + 1 < cols:
                current = max(res[i][j], abs(heights[i][j] - heights[i][j+1]))
                if current < res[i][j+1]:
                    res[i][j+1] = current
                    if present_dict[(i, j + 1)] == False:
                        present_dict[(i, j + 1)] = True
                        queue.append((i, j +1))
            if j - 1 >= 0:
                current = max(res[i][j], abs(heights[i][j] - heights[i][j-1]))
                if current < res[i][j-1]:
                    res[i][j-1] = current
                    if present_dict[(i, j -1)] == False:
                        present_dict[(i, j-1)] = True
                        queue.append((i, j -1))
            present_dict[(i,j)] = False
        return res[rows - 1][cols - 1]
            