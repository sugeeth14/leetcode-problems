class Solution:
    def rob(self, nums: List[int]) -> int:
        
        for i in range(2,len(nums)):
            nums[i] = nums[i] + max(nums[i-2], nums[i-3] if i- 3 >= 0 else 0)
        return max(nums)
        