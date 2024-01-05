class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        sub = []
        
        for i in range(len(nums)):
            if len(sub) == 0 or nums[i] > sub[-1]:
                sub.append(nums[i])
            else:
                index = bisect_left(sub, nums[i])
                sub[index] = nums[i]
        return len(sub)