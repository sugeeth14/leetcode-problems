class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        
        
        
        def dfs(i, j):

            if i < 0 or i == rows or j < 0 or j == cols:
                return
            if grid[i][j] == 0:
                return
            if grid[i][j] == 2:
                return
            grid[i][j] = 2
            dfs(i+ 1, j)
            dfs(i, j + 1)
            dfs(i-1, j)
            dfs(i, j- 1)        
        
        
        for i in range(rows):
            found = False
            for j in range(cols):
                if grid[i][j]:
                    dfs(i, j)
                    found = True
                    break
            if found:
                break
        # print(grid)
        # return 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = "+"
                elif grid[i][j] == 2:
                    grid[i][j] = "-"
        
        # values = [[float("inf")] * cols for _ in range(rows)]
        # return 0
        queue = collections.deque()
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "+":
                    queue.append((i, j, 0))
                    # visited.add((i, j))
        # print(grid)
        # print(queue)
        res = rows * cols
        # print(queue)
        while queue:
            top_i, top_j, level = queue.popleft()
            # print(top_i, top_j, level)
            # if top_i < 0 or top_j < 0 or top_i == rows or top_j == cols:
            #     continue
            
            if grid[top_i][top_j] == "-":
                res = min(res, level)
            if (top_i, top_j) in visited:
                # print(i, j)
                continue
            else:
                visited.add((top_i, top_j))
                # add the neighbors if they are 0
                if top_i + 1 < rows and grid[top_i + 1][top_j] != "+":
                    queue.append((top_i + 1, top_j, level + 1))
                if top_i - 1 >= 0 and grid[top_i - 1][top_j] != "+":
                    queue.append((top_i - 1, top_j, level + 1))
                if top_j + 1 < cols and grid[top_i][top_j + 1] != "+":
                    queue.append((top_i, top_j + 1, level + 1))
                if top_j - 1 >=0 and grid[top_i][top_j-1] != "+":
                    queue.append((top_i, top_j - 1, level + 1))
                # print(queue)
        return res - 1
                
                
            
            
        
        
        
            