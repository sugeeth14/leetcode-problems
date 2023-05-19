class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = collections.defaultdict(int)
        
        for num in nums:
            if num < 0:
                num *= -1
            for i in range(32):
                last_bit = num & 1
                if last_bit:
                    bits[i] += 1
                num >>= 1
        # print(bits)
        ans = 0
        for key in bits:
            if bits[key] % 3 != 0:
                ans = ans + (2**key)
        final_dic = collections.defaultdict(int)
        for num in nums:
            if num == ans or num == -ans:
                final_dic[num] += 1
        
        for key in final_dic:
            if final_dic[key] == 1:
                return key
        
        # print(bits)
        # return ans
        