class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        nums.sort()
        i = 0
        res = 0
        seen = set()
        
        for j in range(len(nums)):
            seen.add(nums[j])
            while nums[i] < nums[j] - len(nums) + 1:
                if nums[i] in seen:
                    seen.remove(nums[i])
                i += 1
            
            
            current = (j - i) + 1 - (j - i + 1 - len(seen))
            # print(current)
            res = max(res, current)
        return len(nums) - res
            
        