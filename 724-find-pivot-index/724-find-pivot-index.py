class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = [0] * len(nums)
        
        moving_sum = 0
        for i in range(len(nums)-1,-1,-1):
            right_sum[i] = moving_sum
            moving_sum += nums[i]
        # print(right_sum)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == right_sum[i]:
                return i
            left_sum += nums[i]
        return -1