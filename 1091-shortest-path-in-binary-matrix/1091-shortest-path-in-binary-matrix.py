class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        ans = [[0] * n for _ in range(n)]
        
        queue = collections.deque()
        
        queue.append([0,0,1]) #i, j and level
        
        visited = set()
        visited.add((0, 0))
        
        directions = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[1,1],[1,-1],[-1,1]]
        while queue:
            i, j, level = queue.popleft()
            if [i,j] == [n-1,n-1]:
                return level
            for x, y in directions:
                if 0<= i + x < n and 0 <= j + y < n and (i + x, j + y) not in visited and grid[i+x][j+y] == 0:
                    visited.add((i + x, j + y))
                    queue.append((i + x, j + y, level + 1))
        return -1
                    
                
            
            
        
        
        