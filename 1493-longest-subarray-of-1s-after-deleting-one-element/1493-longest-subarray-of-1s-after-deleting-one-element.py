class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        Idea
        Have left and right pointers. Keep incrementing right pointer until a maximum of one zero. If you encounter two zeros, calculate the max and increment left pointer until the zeros are again at max one. If there are no zeros in the window, reduce the current window length by 1 before computing the max
        '''
        
        l = 0
        r = 0
        zeros = 0
        
        ans = 0
        
        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
                # check if zeros in the window has reached the limit
                while l < r and zeros > 1:
                    if nums[l] == 0:
                        zeros -= 1
                    l += 1
            window = r - l
            if zeros == 0:
                window -= 1
            ans = max(ans, window)
            r += 1
        
        window = r - l
        # print(r, l)
        # if zeros == 0:
        window -= 1
        ans = max(ans, window)
        return ans
        