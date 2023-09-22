class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        max_window = -1
        target = sum(nums) - x
        l = 0
        
        current = 0
        for r in range(len(nums)):
            current += nums[r]
            
            while l <= r and current > target:
                current -= nums[l]
                l += 1
            
            if current == target:
                max_window = max(max_window, r - l + 1)
        return -1 if max_window == -1 else len(nums) - max_window
        