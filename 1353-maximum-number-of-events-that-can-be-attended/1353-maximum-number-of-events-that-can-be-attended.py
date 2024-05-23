class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: (x[0], x[1]))
        # print(events)
        heap = []
        heapq.heapify(heap)
        i = 0
        res = 0
        for current_time in range(1, 100001):
            while i < len(events) and events[i][0] <= current_time <= events[i][1]:
                heappush(heap, events[i][1])
                i += 1
            # remove outdated events
            # print(heap)
            while heap and heap[0] < current_time:
                heappop(heap)
            
            if heap:
                res += 1
                heappop(heap)
        return res
            
            