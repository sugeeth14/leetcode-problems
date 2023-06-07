class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a != 0 or b != 0 or c != 0:
            last_c = c & 1
            last_a = a & 1
            last_b = b & 1
            if last_c == 0:
                if last_a == 1:
                    ans += 1
                if last_b == 1:
                    ans += 1
            else:
                if last_a == 1 or last_b == 1:
                    pass
                else:
                    ans += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return ans
        