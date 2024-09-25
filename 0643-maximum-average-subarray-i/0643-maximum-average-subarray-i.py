class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        curr = 0
        for i in range(k):
            curr += nums[i]
        
        ans = curr
        
        l = 0
        r = k
        while r < len(nums):
            
            curr -= nums[l]
            curr += nums[r]
            l += 1
            r += 1
            ans = max(ans, curr)
        # ans = max(ans, curr)
        return ans / k
        