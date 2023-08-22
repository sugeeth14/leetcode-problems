class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        cache = {}
        def backtrack(i, m):
            if m == 0:
                return True
            if i == 0:
                return False
            if (i,m) in cache:
                return cache[(i, m)]
            ans = backtrack(i-1,m) or backtrack(i-1,m-nums[i])
            cache[(i,m)] = ans
            return ans
        
        return backtrack(len(nums)-1,target)