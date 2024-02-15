class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        
        left_sum = 0
        
        res = -1
        for i in range(len(nums)):
            if i < 2:
                left_sum += nums[i]
            else:
                if left_sum > nums[i]:
                    res = nums[i] + left_sum
                left_sum += nums[i]
        return res
                
        