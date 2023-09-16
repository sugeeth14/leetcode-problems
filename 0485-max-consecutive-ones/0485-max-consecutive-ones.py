class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        current = 0
        for num in nums:
            if num == 0:
                res = max(res, current)
                current = 0
            else:
                current += 1
        res = max(current, res)
        return res
        