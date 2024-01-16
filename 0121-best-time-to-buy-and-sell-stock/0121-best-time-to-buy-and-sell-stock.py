class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_left = prices[0]
        ans = 0
        
        for i in range(len(prices)):
            ans = max(ans, prices[i] - min_left)
            min_left = min(min_left, prices[i])
        return ans
        