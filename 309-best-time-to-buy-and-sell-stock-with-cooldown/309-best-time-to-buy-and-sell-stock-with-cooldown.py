class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # sell = i + 2
        # buy = i + 1
        
        dp = {}
        @lru_cache(maxsize=None)
        def dfs(i, buying):
            if (i, buying) in dp:
                return dp[(i, buying)]
            if i >= len(prices):
                dp[(i, buying)] = 0
                return 0
            else:
                if buying:
                    buy = dfs(i + 1, not buying) - prices[i]
                    cooldown = dfs(i + 1, buying)
                    dp[(i, buying)] = max(buy, cooldown)
                else:
                    sell = dfs(i + 2, not buying) + prices[i]
                    cooldown = dfs(i+1, buying)
                    dp[(i, buying)] = max(cooldown, sell)
                return dp[(i, buying)]
        return dfs(0, True)