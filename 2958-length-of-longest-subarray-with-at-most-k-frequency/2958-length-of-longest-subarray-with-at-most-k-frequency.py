class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        '''
        Algorithm:
        1. Start with left pointer initialized to zero and dicionary to keep the count
        2. Start iterating with right pointer and every time a value is added check the dictionary to see if the value has reached k
        3. If it has exceeded k, move the left pointer until the value is equal to k
        4. Calculate this window size using r - l + 1 and update the res
        5. Return the res
        '''
        l = 0
        dic = collections.defaultdict(int)
        
        
        res = 0
        for r in range(len(nums)):
            dic[nums[r]] += 1
            while dic[nums[r]] > k:
                dic[nums[l]] -= 1
                l += 1
            # at this point calculate the window size
            window = r - l + 1
            res = max(res, window)
        return res
        