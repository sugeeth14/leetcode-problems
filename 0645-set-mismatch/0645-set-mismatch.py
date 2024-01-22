class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        res = []
        seen = set()
        
        for i in range(len(nums)):
            if nums[i] in seen:
                res.append(nums[i])
            seen.add(nums[i])
        
        for i in range(1, len(nums) + 1):
            if i not in seen:
                res.append(i)
                break
        return res
        
        
        