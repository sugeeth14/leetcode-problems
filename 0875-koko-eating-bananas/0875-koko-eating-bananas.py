class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        def gethours(n):
            res = 0
            for pile in piles:
                res = res + math.ceil(pile/n)
            return res
        # print(gethours(8))
        l = 1
        r = max(piles)
        while l <= r:
            mid = (l + r)//2
            hours = gethours(mid)
            if hours > h:
                l = mid + 1
            else:
                r = mid - 1
                ans = mid
        return ans