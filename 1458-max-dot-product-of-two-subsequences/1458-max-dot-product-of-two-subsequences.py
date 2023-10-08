class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        rows = len(nums1)
        cols = len(nums2)
        
        dp = [[0] * cols for _ in range(rows)]
        # print(dp)
        res = -inf
        
        for i in range(rows):
            for j in range(cols):
                # for everything we have three cases
                #1. if max value is at (i-1,j)
                val1 = dp[i-1][j] if i-1 >= 0 else -inf
                val2 = dp[i][j-1] if j-1 >=0 else -inf
                val3 = dp[i-1][j-1] if (i-1) >=0 and (j-1) >=0 else -inf
                
                val3 = max(val3,0) + (nums1[i] * nums2[j])
                dp[i][j] = max(val1, val2, val3)
                res = max(res, dp[i][j])
        return res
        
        
        