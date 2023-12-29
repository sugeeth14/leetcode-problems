class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = 0
        
        for i in range(len(prices) - 2, -1, -1):
            dp += max(0, prices[i+1] - prices[i])
        
        return dp