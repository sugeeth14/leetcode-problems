class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        l = 0
        res = []
        while l < len(nums):
            # new_target = 0 - nums[l]
            start = l + 1
            end = len(nums) - 1
            while start < end:
                total_sum = nums[l] + nums[start] + nums[end]
                if total_sum == 0:
                    res.append([nums[l], nums[start], nums[end]])
                    start += 1
                    while start < len(nums) and nums[start] == nums[start - 1]:
                        start += 1
                elif total_sum < 0:
                    start += 1
                else:
                    end -= 1
            # Move left until it is not equal to previous
            l += 1
            while l < len(nums) and nums[l] == nums[l - 1]:
                l += 1
        return res
                        
        