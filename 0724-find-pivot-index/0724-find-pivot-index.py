class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            if i != 0:
                left += nums[i-1]
                total -= nums[i-1]
            if left == total - nums[i]:
                return i
        return -1
            
            
        