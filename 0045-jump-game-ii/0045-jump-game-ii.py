class Solution:
    def jump(self, nums: List[int]) -> int:
        
        
        ans = [0] * len(nums)
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= len(nums) - 1:
                # can reach last index
                ans[i] = 1
            else:
                #check the min in the possible children
                min_value = inf
                for j in range(i+1, min(nums[i] + i + 1, len(nums))):
                    min_value = min(min_value, ans[j])
                
                ans[i] = 1 + min_value
        # print(ans)
        return ans[0]
        