class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set()
        
        for num in nums:
            seen.add(num)
        
        for i in range(len(nums) + 1):
            if i not in seen:
                return i
        