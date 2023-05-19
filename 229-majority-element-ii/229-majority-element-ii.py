class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        dic = collections.defaultdict(int)
        
        for num in nums:
            dic[num] += 1
        
        threshold = len(nums)//3
        res = []
        
        res_set = set()
        
        for num in nums:
            if dic[num] > threshold and num not in res_set:
                res.append(num)
                res_set.add(num)
        return res
        