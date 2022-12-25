class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        
        res = []
        for q in queries:
            ans = 0
            moving_sum = 0
            for i in range(len(nums)):
                moving_sum += nums[i]
                if moving_sum > q:
                    break
                else:
                    ans += 1
            res.append(ans)
        return res
                
            
        