class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        current = 0
        
        for i in range(len(gain)):
            current += gain[i]
            res = max(current, res)
        return res
        