class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        mod = 1000000007
        h = []
        heapq.heapify(h)
        # print(h)
        for i in range(len(nums)):
            heapq.heappush(h, nums[i])
        while k!=0:
            top = heapq.heappop(h)
            # print(top)
            top += 1
            k -= 1
            heapq.heappush(h,top)
        res = 1
        while h:
            res *= heapq.heappop(h)
            res %=mod
        return res % mod
                
        