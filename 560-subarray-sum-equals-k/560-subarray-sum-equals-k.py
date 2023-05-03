class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            prefix_sum.append(total)
        # come in reverse
        # print(prefix_sum)
        from collections import defaultdict
        ans = 0
        dic = defaultdict(int)
        for i in range(len(nums) -1, -1, -1):
            new_target = prefix_sum[i] + k
            ans += dic[new_target]
            dic[prefix_sum[i]] += 1
            # print(ans, dic)
        ans += dic[k]
        return ans
        
        