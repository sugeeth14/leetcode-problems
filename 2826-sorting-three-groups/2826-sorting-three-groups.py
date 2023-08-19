class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        last_seen = {}
        ans = [1] * len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 1:
                if 1 in last_seen:
                    ans[i] = max(ans[i],ans[last_seen[1]] + 1)
                if 2 in last_seen:
                    ans[i] = max(ans[i], ans[last_seen[2]] + 1)
                if 3 in last_seen:
                    ans[i] = max(ans[i], ans[last_seen[3]] + 1)
            elif nums[i] == 2:
                if 2 in last_seen:
                    ans[i] = max(ans[i], ans[last_seen[2]] + 1)
                if 3 in last_seen:
                    ans[i] = max(ans[i], ans[last_seen[3]] + 1)
            else:
                if 3 in last_seen:
                    ans[i] = max(ans[i], ans[last_seen[3]] + 1)
            
            last_seen[nums[i]] = i
        # print(ans)
        return len(nums) - max(ans)
                
                
        