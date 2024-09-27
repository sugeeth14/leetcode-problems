class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        zeros = 0
        l = 0
        r = 0
        ans = 0
        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            r += 1
            while l < r and zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            ans = max(ans, r - l)
            # print(l, r)
        return ans
            
        