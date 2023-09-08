class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = {}
        
        res = 0
        
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
            if (nums[i] + 1) not in dic and (nums[i] - 1) not in dic:
                continue
            else:
                # print("printing",nums[i] + 1, nums[i]-1)
                res = max(res, max(dic.get(nums[i]+1, 0), dic.get(nums[i]-1,0)) + dic[nums[i]])
            # print(nums[i],res)
        return res