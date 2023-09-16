class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = collections.defaultdict(int)
        res = 0
        for num in nums:
            res = res + dic[num]
            dic[num] += 1
        return res
        