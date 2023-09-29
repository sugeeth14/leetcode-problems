class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        first = nums[0]
        last = nums[-1]
        
        if first == last:
            status = 0
        elif last > first:
            status = 1
        else:
            status = 2
            
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if status == 0:
                if diff != 0:
                    return False
            elif status == 1:
                if diff < 0:
                    return False
            elif status == 2:
                if diff > 0:
                    return False
        return True
        