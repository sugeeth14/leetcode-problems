class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        l = 0
        product = 1
        ans = 0
        
        for r in range(len(nums)):
            product *= nums[r]
            while l <=r and product >= k:
                product /= nums[l]
                l += 1
            if r > l:
                ans += (r - l)
            
            if nums[r] < k:
                ans += 1
            # print(nums[r], ans, l, r)
        return ans
                
            
            
        