class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        nums.sort()
        
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == k:
                ans += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < k:
                # increment l
                l += 1
            else:
                r -= 1
        return ans
        