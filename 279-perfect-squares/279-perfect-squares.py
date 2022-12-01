class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0
        squares = []
        for i in range(math.ceil(math.sqrt(n)) + 1):
            squares.append(i * i)
        # print(squares)
        for target in range(1, n + 1):
            # For every value we should see what is the best for it
            for square in squares:
                if target < square:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])
        return dp[n]
            
        