class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        l = 0
        r = len(nums) - 1
        ans = 0
        mod = 1000000007
        
        while l <=r:
            if (nums[l] + nums[r] > target):
                r -= 1
            else:
                ans = ans + ((2**(r-l)) % mod)
                l += 1
        return ans % mod
        