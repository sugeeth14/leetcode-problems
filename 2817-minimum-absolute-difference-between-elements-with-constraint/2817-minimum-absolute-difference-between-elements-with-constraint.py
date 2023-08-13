import sortedcontainers
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        
        j = len(nums) - 1
        i = j - x
        
        s = sortedcontainers.SortedList()
        
        # print(i, j)
        res = inf
        while i >= 0:
            s.add(nums[j])
            index = s.bisect_left(nums[i])
            
            if index > 0:
                res = min(res, nums[i] - s[index-1])
            if index < len(s):
                res = min(res, s[index] - nums[i])
            
            i -= 1
            j -= 1
        return res
            
        