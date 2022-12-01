class Solution:
    def numSquares(self, n: int) -> int:
        
        all_squares = []
        for i in range(101):
            all_squares.append(i * i)
        all_squares_set = set(all_squares)
        
        @lru_cache(maxsize=None)
        def backtrack(rem):
            if rem == 0:
                return 1
            if rem in all_squares_set:
                return 1
            val_min = 100
            for i in range(len(all_squares)-1,0,-1):  
                if rem - all_squares[i] >= 0:
                    first_operand = rem-all_squares[i]
                    second_operand = all_squares[i]
                    val = backtrack(first_operand) + backtrack(second_operand)
                    val_min = min(val, val_min)
                    if val_min == 2:
                        break
            return val_min
        return backtrack(n)
                
        