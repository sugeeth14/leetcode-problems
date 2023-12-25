class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Algorithm
        1. Start from index 2
        2. Set the variable last to 2
        3. If the current value is equal to the last -2 index, do nothing and continue
        4. Else, swap the number with last index and incremetn last
        5. Return last at the end
        """
        if len(nums) <= 1:
            return len(nums)
        last = 0
        ptr1 = 0
        ptr2 = 0
        while ptr2 < len(nums):
            while ptr2 < len(nums) and nums[ptr2] == nums[ptr1]:
                ptr2 += 1
            width = ptr2 - ptr1
            for i in range(min(2, width)):
                nums[last + i] = nums[ptr1]
            last = last + min(2, width)
            ptr1 = ptr2
        return last
            
        