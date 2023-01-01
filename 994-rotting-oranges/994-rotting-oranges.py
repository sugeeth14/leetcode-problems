class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Every time look at the neighbors and keep marking them by adding them into a queue
        
        
        from collections import deque
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        # First add all the rotten oranges to the queue as that will be the starting point
        visited = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    # visited.add((i, j))
        # Once queue is ready you can keep popping from the queue and mark every of the oranges adjacent as rotten
        
        res = 0
        
        while q:
            row, column, minute = q.popleft()
            if row < 0 or column < 0 or row == rows or column == cols:
                continue
            if (row, column) in visited:
                continue
            # if grid[i][j] == 1 or grid[i][j] == 0:
            #     continue
            else:
                visited.add((row, column))
                if grid[row][column] == 0:
                    continue
                # Mark the orange as rotten
                grid[row][column] = 2
                # Add the neighbors
                res = max(res, minute)
                q.append((row + 1, column, minute + 1))
                q.append((row - 1, column, minute + 1))
                q.append((row, column + 1, minute + 1))
                q.append((row, column - 1, minute + 1))
        # After all of them are marked check if there are any fresh oranges yet
        # print(grid)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        # Else return res
        return res
                
                
            
            
        