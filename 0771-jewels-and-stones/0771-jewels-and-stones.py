class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(list(jewels))
        # print(jewels)
        res = 0
        for stone in stones:
            res += stone in jewels
        return res
        