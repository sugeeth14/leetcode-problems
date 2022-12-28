class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h = []
        heapq.heapify(h)
        for pile in piles:
            heappush(h, -1 * pile)
        # print(h)
        while k:
            top = heappop(h)
            top //= 2
            heappush(h, top)
            k -= 1
        return -1 * sum(h)
        
        