class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0
        while xor:
            last_bit = xor & 1
            count += last_bit
            xor >>= 1
        return count
            
        