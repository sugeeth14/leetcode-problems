class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.defaultdict(int)
        for num in nums:
            dic[num] += 1
        res = []
        for key in sorted(dic, key=dic.get, reverse=True):
            res.append(key)
            k -= 1
            if k == 0:
                return res
