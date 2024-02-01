class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        ans = []
        nums.sort()
        
        i = 0
        
        while i < len(nums):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            
            if c - a > k:
                return []
            ans.append([a, b, c])
            i += 3
        
        return ans
        