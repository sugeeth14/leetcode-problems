class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Algorithm
        # 1. Go through each element of nums
        # 2. Whenever you encounter and element equal to val place it at the last and swap the last with the current element
        # 3. decrement last and repeat the process 
        # 4. If the element is not equal increment k. 
        # 5. Do this until k <= last break out once k exceeds last.
        if len(nums) == 0:
            return 0
        last = len(nums) - 1
        k = 0
        while k <= last:
            if nums[k] == val:
                nums[k], nums[last] = nums[last], nums[k]
                last -= 1
            else:
                k += 1
        
        return k
        