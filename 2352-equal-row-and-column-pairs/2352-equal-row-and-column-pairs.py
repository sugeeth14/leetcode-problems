class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        dic = collections.defaultdict(int)
        
        rows = len(grid)
        cols = rows
        
        for i in range(rows):
            dic[tuple(grid[i])] += 1
            
            
        ans = 0
        
        for i in range(cols):
            current_col = []
            for j in range(rows):
                current_col.append(grid[j][i])
            if tuple(current_col) in dic:
                ans += dic[tuple(current_col)]
        return ans
        