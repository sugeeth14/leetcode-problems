class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_prefix = [1] * len(nums)
        
        
        for i in range(1, len(nums)):
            left_prefix[i] = left_prefix[i-1] * nums[i-1]
        
        
        right_product = 1
        for i in range(len(nums) - 1, -1 , -1):
            left_prefix[i] = right_product * left_prefix[i]
            right_product *= nums[i]
        
        return left_prefix
            
        