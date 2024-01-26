class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        '''
        Algorithm:
        1. From the start or every position you have 4 choices.
        2. You backtrack in all 4 directions.
        3. At every stage you see if the moves remaining is not zero if zero return 0 possibility.
        4. Once you reach the out of bounds, return 1 as the possiblity
        5. For every position add the 4 values in 4 directions and return the  result.
        6. Keep in cache, the current position index and number of positions remaining.
        '''
        
        
        cache = {}
        mod = 1000000007
        
        
        def backtrack(i, j, moves_left):
            if i == -1 or i == m or j == -1 or j == n:
                # reached out of bounds return 1
                return 1
            if moves_left == 0:
                return 0
            if (i, j, moves_left) in cache:
                return cache[(i, j, moves_left)]
            
            res = (backtrack(i+1,j, moves_left - 1) + backtrack(i-1,j, moves_left - 1) + backtrack(i,j+1, moves_left - 1) + backtrack(i,j-1, moves_left - 1)) % mod # explore all 4 positions
            cache[(i,j,moves_left)] = res
            return res
        
        ans = backtrack(startRow, startColumn, maxMove)
        return ans % mod
            
        