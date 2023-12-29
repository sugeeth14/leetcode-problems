class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_true = len(nums) - 1
        
        for i in range(len(nums)-2,-1,-1):
            if nums[i] + i >= last_true:
                last_true = i
        
        return last_true == 0
        