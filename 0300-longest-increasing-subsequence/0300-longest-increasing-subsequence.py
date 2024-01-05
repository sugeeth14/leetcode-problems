class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            max_val = 0
            for j in range(i-1,-1,-1):
                if nums[i] > nums[j]:
                    max_val = max(max_val, dp[j])
            
            dp[i] += max_val
        return max(dp)