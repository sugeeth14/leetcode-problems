class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right_max = prices[-1]
        res = 0
        for i in range(len(prices) -2, -1, -1):         
            res = max(right_max - prices[i], res)
            right_max = max(prices[i], right_max)
        return res
            
            
        