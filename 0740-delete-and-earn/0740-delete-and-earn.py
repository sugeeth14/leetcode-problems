class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dic = collections.defaultdict(int)
        
        for i in range(len(nums)):
            dic[nums[i]]+=nums[i]
        
        # print(dic)
        ans = 0
        
        for key in range(min(dic.keys()),max(dic.keys()) + 1):
            dic[key] = dic[key] + max(dic[key-2] if (key-2) in dic else 0, dic[key-3] if (key-3) in dic else 0)
            ans = max(ans, dic[key])
        return ans
            
        