class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        factor = 0
        while num:
            lsb = num & 1
            if lsb:
                pass
            else:
                ans = ans + (1 << factor)
            factor += 1
            num >>=1
        return ans
            
        