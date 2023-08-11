class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        ans = [[0] * (len(coins) +1) for _ in range(amount+1)]
        # print(ans)
        for i in range(1, len(coins) + 1):
            ans[0][i] = 1
        
        # print(ans)
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                ans[j][i]  = ans[j][i-1]
                # print(i)
                if j - coins[i-1] >= 0:
                    ans[j][i] += ans[j - coins[i-1]][i]
        # print(ans)
        return ans[amount][len(coins)]
                
        