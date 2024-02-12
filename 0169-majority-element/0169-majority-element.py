class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        value = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == value:
                count += 1
            else:
                if count == 0:
                    value = nums[i]
                    count = 1
                else:
                    count -= 1
        return value
        