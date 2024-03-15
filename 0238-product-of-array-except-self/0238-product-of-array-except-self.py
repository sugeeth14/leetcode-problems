class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_product = [1]
        for i in range(1, len(nums)):
            left_product.append(nums[i-1] * left_product[-1])
        
        right_product = 1
        ans = [1] * len(nums)
        for i in range(len(nums)- 1, -1, -1):
            ans[i] = left_product[i] * right_product
            right_product *= nums[i]
        return ans
        