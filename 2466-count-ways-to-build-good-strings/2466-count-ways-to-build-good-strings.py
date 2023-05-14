class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        dp = {}
        mod = 1000000007
        
        def backtrack(index):
            if index < 0:
                return 0
            elif index == 0:
                return 1
            elif index in dp:
                return dp[index]
            else:
                ans = (backtrack(index - zero) % mod + backtrack(index - one) % mod) % mod
                dp[index] = ans % mod
                return dp[index]
         
        res = 0
        for i in range(high, low - 1, -1):
            res = (res + backtrack(i)) % mod
        return res % mod
            
                
            
            
            
        