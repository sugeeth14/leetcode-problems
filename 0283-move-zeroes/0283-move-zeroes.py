class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # start by moving all non zero to the front, make all zeros later
        insert = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert] = nums[i]
                insert += 1
        for i in range(insert, len(nums)):
            nums[i] = 0

        