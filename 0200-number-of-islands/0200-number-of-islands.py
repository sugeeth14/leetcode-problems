class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Algorithm:
        1. Maintain a set of visited.
        2. Iterate over the rows and columns of the grid.
        3. If the current index is 1 and it is not in visited, call backtrack function and add 1 to the res
        4. Inside the backtrack function, if the current index is not in visited add to visited, only if the current index has 1 in it else return
        5. Call backtrack with all its neighbors.
        6. Return the res at the end after iterating all the indices in the grid
        '''
        
        
        res = 0
        
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        
        def backtrack(x, y):
            if (x, y) in visited:
                return
            if x < 0 or x == rows or y < 0 or y == cols:
                return
            if grid[x][y] == "0":
                return
            visited.add((x, y))
            backtrack(x + 1, y)
            backtrack(x, y + 1)
            backtrack(x - 1, y)
            backtrack(x, y - 1)
        
        for x in range(rows):
            for y in range(cols):
                if (x, y) not in visited and grid[x][y] == "1":
                    res += 1
                    backtrack(x, y)
        return res
        