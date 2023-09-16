class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        neighbors = collections.defaultdict(dict)
        for i in range(len(edges)):
            neighbors[edges[i][0]][edges[i][1]] = succProb[i]
            neighbors[edges[i][1]][edges[i][0]] = succProb[i]
        
        heap = []
        res = {}
        heapify(heap)
        heappush(heap, (-1, start_node))
        
        while heap:
            distance, node = heappop(heap)
            # print(distance, node)
            if node in res:
                continue
            res[node] = distance
            
            for neighbor in neighbors[node]:
                if neighbor not in res:
                    heappush(heap, (distance * neighbors[node][neighbor], neighbor))
        # print(res)
        return -res[end_node] if end_node in res else 0