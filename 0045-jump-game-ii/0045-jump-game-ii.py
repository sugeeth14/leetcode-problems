class Solution:
    def jump(self, nums: List[int]) -> int:
        
        
        
        l = 0
        r = 0
        res = 0
        while r < len(nums) - 1:
            max_distance = 0
            for i in range(l, r + 1):
                max_distance = max(max_distance, nums[i] + i)
            
            res += 1
            l = r + 1
            r = max_distance
        
        return res
        