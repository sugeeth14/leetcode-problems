class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        '''
        Algorithm
        1. We will be doing this as a sliding window approach
        2. Initialize two pointers l and r
        3. Keep incrementing r and when you reach the number of zeros in between greater than k stop.
        4. Keep incrementing l until it reaches r and stop if it overcomes it. 
        5. At every stage keep count of the maximum window by calculating r - l + 1 if the number of zeros in the range are <= k
        '''
        
        l = 0
        ans = 0
        
        current = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                current += 1
            
            while l <= i and current > k:
                if nums[l] == 0:
                    current -= 1
                l += 1
            
            ans = max(ans, i - l + 1)
        return ans
                        
            
        