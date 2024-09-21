class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        left_product = []
        for i in range(len(nums)):
            left_product.append(product)
            product *= nums[i]
        
        product = 1
        right_product = [1] * len(nums)
        for i in range(len(nums) -1, -1, -1):
            right_product[i] = product
            product *= nums[i]
        
        # print(left_product, right_product)
        res = []
        for i in range(len(nums)):
            res.append(left_product[i] * right_product[i])
        return res
        