class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        s += s
        goal += goal
        
        dp = [[0] * len(goal) for _ in range(len(s))]
        
        # print(dp)
        max_value = 0
        for i in range(len(s)):
            for j in range(len(goal)):
                if s[i] == goal[j]:
                    dp[i][j] = 1 + (dp[i-1][j-1] if i > 0 and j > 0 else 0)
                max_value = max(max_value, dp[i][j])
        
        
        
        return max_value >= len(s)//2
        