class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 2:
            return max(nums)
        
        res = [nums[0], nums[1]]
        for i in range(2, len(nums)-1):
            res.append(nums[i] + max(res[i-2] if (i-2) >= 0 else 0, res[i-3] if (i-3) >= 0 else 0))
        # print(res)
        res2 = [0, nums[1]]
        for i in range(2, len(nums)):
            res2.append(nums[i] + max(res2[i-2] if (i-2) >= 1 else 0, res2[i-3] if (i-3) >= 1 else 0))
        # print(res, res2)
        return max(max(res) , max(res2))
        