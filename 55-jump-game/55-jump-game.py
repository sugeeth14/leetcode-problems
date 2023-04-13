class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastTrue = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= lastTrue:
                lastTrue = i
        if lastTrue == 0:
            return True
        return False
                        
                    
                
            
            
        