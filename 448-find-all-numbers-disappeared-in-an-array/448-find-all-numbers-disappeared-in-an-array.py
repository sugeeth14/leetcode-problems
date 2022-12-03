class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        i = 1
        j = 0
        # print(nums)
        while j < len(nums):
            if nums[j] > i:
                res.append(i)
                i += 1
            elif nums[j] == i:
                i += 1
                j += 1
            else:
                j += 1
        for k in range(i, len(nums) + 1):
            res.append(k)
        return res
    
        
            
            
        
        