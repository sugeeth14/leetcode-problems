class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        ans = 0
        for i in range(k):
            ans += nums[i]
        max_ans = ans
        for i in range(k, len(nums)):
            ans += nums[i]
            ans -= nums[i-k]
            max_ans = max(max_ans, ans)
            # print(max_ans)
        return max_ans/k
        