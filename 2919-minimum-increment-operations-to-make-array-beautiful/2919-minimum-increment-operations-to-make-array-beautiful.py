class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        
        dp = [0] * len(nums)
        for i in range(3):
            dp[i] = max(0, k - nums[i])
        
        for i in range(3, len(nums)):
            dp[i] = max(0, k - nums[i]) + min(dp[i-1],dp[i-2],dp[i-3])
        return min(dp[-1],dp[-2],dp[-3])
        
        
        