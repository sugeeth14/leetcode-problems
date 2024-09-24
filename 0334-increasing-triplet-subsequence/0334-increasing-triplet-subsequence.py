class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        # For every number maintain left min and right max
        
        left_min = [nums[0]]
        curr = nums[0]
        for i in range(1, len(nums)):
            left_min.append(curr)
            curr = min(nums[i], curr)
        # print(left_min)
        right_max = [nums[-1]] * len(nums)
        curr = nums[-1]
        for i in range(len(nums) - 1, -1, -1):
            right_max[i] = curr
            curr = max(curr, nums[i])
        # print(right_max)
        for i in range(1, len(nums) - 1):
            if left_min[i] < nums[i] < right_max[i]:
                return True
        return False
            
        