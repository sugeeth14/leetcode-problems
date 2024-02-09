class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        '''
        Algorithm:
        1. Sort the nums
        2. Create a res = [1] times size of nums
        3. For each num in nums go backward and explore all numbers that are divisible by the current number and of them find the one that has the greatest value in res and add 1 to it as the res of current number
        4. At the end find the max value of res and the number corresponding to it. 
        5. keep coming back until you find all the numbers that form the sequence
        '''
        
        nums.sort()
        res = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i-1,-1,-1):
                if nums[i] % nums[j] == 0:
                    res[i] = max(res[i], res[j] + 1)
        
        ans = []
        
        count = max(res)
        value = nums[res.index(count)]
        
        i = len(nums) - 1
        while count > 0:
            # print(i)
            if res[i] == count and value % nums[i] == 0:
                ans.append(nums[i])
                value = nums[i]
                
                count -= 1
                # print(ans, count)
            i -= 1
        return ans[::-1]
            
        