class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        i = 0
        j = 0
        
        res = []
        
        current = 0
        while current < len(nums):
            if current % 2 == 0:
                while nums[i] < 0:
                    i += 1
                res.append(nums[i])
                i += 1
            else:
                while nums[j] > 0:
                    j += 1
                res.append(nums[j])
                j += 1
            current += 1
        return res
            
            
        