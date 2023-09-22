class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        ans = inf
        
        current = 0
        for i in range(len(nums)):
            current += nums[i]
            if current >= x:
                break
        # print(i)
        j = len(nums) - 1
        while i >= 0:
            # print(i, j)
            if current == x:
                ans = min(ans, len(nums)-1-j + i + 1)
            current -= nums[i]
            i -= 1
            while current < x and j > i:
                current += nums[j]
                j -= 1
            # i -= 1
        # print(current)
        if current == x:
            ans = min(ans, len(nums)-1-j + i + 1)
        return ans if ans != inf else -1
        