class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        forward_moving_averages = [0] * len(nums)
        moving_sum = 0
        for i in range(len(nums)):
            moving_sum += nums[i]
            forward_moving_averages[i] = moving_sum // (i + 1)
        # print(forward_moving_averages)
        reverse_moving_averages = [0] * len(nums)
        moving_sum = nums[-1]
        for i in range(len(nums) -2, -1, -1):
            reverse_moving_averages[i] = moving_sum //(len(nums) - i-1)
            moving_sum += nums[i]
        res = abs(forward_moving_averages[0] - reverse_moving_averages[0])
        res_index = 0
        for i in range(1, len(nums)):
            if abs(forward_moving_averages[i] - reverse_moving_averages[i]) < res:
                res = abs(forward_moving_averages[i] - reverse_moving_averages[i])
                res_index = i
        return res_index
            
        