class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        '''
        Algorithm:
        1. We will be doing this in dp
        2. At every row, from where left or right is there, we will expolore non overlappling directions for both the robots.
        3. We will then calculate for the sub problem what is the best possible solution.
        4. We will cache the result at each step by caching row, column1, and column2
        5. Once we reach the end we return 0
        '''
        
        
        rows = len(grid)
        cols = len(grid[0])
        
        cache = {}
        
        def backtrack(row, column1, column2):
            if (row, column1, column2) in cache:
                return cache[(row, column1, column2)]
            if column1 < 0 or column1 == cols or column2 < 0 or column2 == cols:
                return 0 # out of bounds so no result is possible
            if row == rows:
                return 0 # We have reached the terminting condition or base case.
            best_res = 0
            for i in [column1, column1 + 1, column1 - 1]:
                for j in [column2, column2 + 1, column2 - 1]:
                    if i != j:
                        best_res = max(best_res, backtrack(row + 1, i, j) + grid[row][column1] + grid[row][column2])
            cache[(row, column1, column2)] = best_res
            return best_res
        
        return backtrack(0, 0, cols - 1)
                        
        