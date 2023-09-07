class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        neighbors = collections.defaultdict(dict)
        
        for time in times:
            neighbors[time[0]][time[1]] = time[2]
        # print(neighbors)
        
        heap = []
        # heapify(heap)
        for i in range(1, n + 1):
            heappush(heap, (inf, i))
        # print(heap)
        heappush(heap, (0, k)) # set the source vertex distance to 0
        res = {}
        
        while heap:
            distance, node = heappop(heap)
            # print(distance, node)
            # add the node to the result set if not present
            if node in res:
                continue
            res[node] = distance
            for neighbor in neighbors[node]:
                if neighbor not in res:
                    heappush(heap, (distance + neighbors[node][neighbor], neighbor))
        return max(res.values()) if max(res.values()) != inf else -1     
        