class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        '''
        Algorithm:
        1. For each index in nums, precompute the num - reverse and store it in an array.
        2. Iterate over every index and check if the current num - reverse has occurrent how many times, add that to the res after modding. 
        3. Add the current presum to the dic
        '''
        
        
        def get_reverse(num):
            reverse = 0
            while num:
                reverse = (reverse * 10) + (num % 10)
                num = num // 10
            # print(reverse)
            return reverse
                
        
        prefix = []
        
        for i in range(len(nums)):
            reverse = get_reverse(nums[i])
            # print(reverse)
            diff = nums[i] - reverse
            prefix.append(diff)
        
        # print(prefix)
        res = 0
        mod = 1000000007
        dic = collections.defaultdict(int)
        for i in range(len(prefix)):
            res = (res + (dic[prefix[i]] % mod)) % mod
            dic[prefix[i]] += 1
        return res
        