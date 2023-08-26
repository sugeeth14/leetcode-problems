class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        col = set()
        pos_diag = set() # (r + c)
        neg_diag = set() # (r - c)
        
        board = [["."] * n for _ in range(n)]
        
        res = []
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r - c) in neg_diag or (r + c) in pos_diag:
                    continue
                
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"
                
                backtrack(r + 1)
                
                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."
        backtrack(0)
        return res
                    
        