class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        heapq.heapify(h)
        for stone in stones:
            heappush(h, -stone)
        # print(h)
        while len(h) > 1:
            top1, top2 = heappop(h), heappop(h)
            if top1 == top2:
                continue
            else:
                heappush(h, top1 - top2)
        if h:
            return -h[0]
        else:
            return 0
        