class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ptr1 = 0
        ptr2 = 0
        if sum(nums) < target:
            return 0
        
        
        current_sum = 0
        res = float("infinity")
        
        while ptr2 < len(nums):
            if current_sum >= target:
                res = min(ptr2 - ptr1, res)
                current_sum -= nums[ptr1]
                ptr1 += 1
            else:
                current_sum += nums[ptr2]
                ptr2 += 1
        while ptr1 < len(nums) and current_sum >=target:
            res = min(ptr2 - ptr1, res)
            current_sum -= nums[ptr1]
            ptr1 += 1
        return res
                
                
                
        