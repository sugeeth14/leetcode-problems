class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = collections.defaultdict(int)
        
        prefix_sum = 0
        ans = 0
        dic[prefix_sum] = 1
        for num in nums:
            prefix_sum += num
            ans += dic[prefix_sum - k]
            dic[prefix_sum] += 1
        return ans
            
        