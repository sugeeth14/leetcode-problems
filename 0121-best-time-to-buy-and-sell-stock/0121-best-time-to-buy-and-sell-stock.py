class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_min = prices[0]
        ans = 0
        
        for i in range(1, len(prices)):
            ans = max(ans, prices[i] - left_min)
            left_min = min(prices[i], left_min)
        return ans
        