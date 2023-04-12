class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        local_sum = nums[0]
        for i in range(1, len(nums)):
            local_sum = max(nums[i], local_sum + nums[i])
            max_sum = max(local_sum, max_sum)
        return max_sum
        