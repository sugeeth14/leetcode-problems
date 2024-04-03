class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        
        visited = set()
        
        rows = len(board)
        cols = len(board[0])
        def backtrack(i, j, index):
            # print(i, j, index)
            if (i, j) in visited:
                return False
            if i >= rows or j >= cols or i < 0 or j < 0:
                return False
            
            
            
            if word[index] != board[i][j]:
                return False
            if index == len(word) - 1:
                return True
            visited.add((i, j))
            res = backtrack(i + 1, j, index + 1) or backtrack(i - 1, j, index + 1) or backtrack(i, j + 1, index + 1) or backtrack(i, j - 1, index + 1)
            visited.remove((i, j))
            # print(res)
            return res
        
        for i in range(rows):
            for j in range(cols):
                res = backtrack(i, j, 0)
                # print(res)
                if res:
                    return True
        return False
        