class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        dic = collections.defaultdict(int)
        
        for i in range(len(nums)):
            dic[nums[i]] += 1
        
        res = 0
        
        for value in dic.values():
            if value == 1:
                return -1
            else:
                while value % 3 != 0:
                    value -= 2
                    res += 1
                res = res + (value)//3
        return res
            
        