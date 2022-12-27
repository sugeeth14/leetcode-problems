class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # return True
        if len(nums) == 1:
            return False
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        m = nums_sum//2
        dp = [[0] * (m+1) for _ in range(len(nums) + 1)]
        for i in range(1, m + 1):
            dp[0][i] = 0
        for i in range(len(nums) + 1):
            dp[i][0] = 1
        # print(dp)
        
        for i in range(1, len(nums) + 1):
            for j in range(1, m + 1):
                # print(i, j)
                if j - nums[i-1] >= 0:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i-1]])
                else:
                    dp[i][j] = dp[i-1][j]
            if dp[i][m]:
                # print(dp)
                return dp[i][m]
        
        return False
            
        
        