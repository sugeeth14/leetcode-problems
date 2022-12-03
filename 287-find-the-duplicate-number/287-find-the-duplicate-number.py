class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start = nums[0]
        while True:
            if nums[0] == nums[start]:
                return nums[0]
            start = nums[0]
            nums[0], nums[start] = nums[start], nums[0]
            
            
            
        