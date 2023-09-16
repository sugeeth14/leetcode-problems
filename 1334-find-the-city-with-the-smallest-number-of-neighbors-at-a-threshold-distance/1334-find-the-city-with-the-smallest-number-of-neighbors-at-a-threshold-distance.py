class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # initialize distance map that is common for all edges
        distance = {}
        neighbors = collections.defaultdict(dict)
        for edge in edges:
            neighbors[edge[0]][edge[1]] = edge[2]
            neighbors[edge[1]][edge[0]] = edge[2]
        
        heap = []
        heapq.heapify(heap)
        
        for i in range(n):
            heappush(heap, (0, i, i))
        
        while heap:
            length, src, dest = heappop(heap)
            if length > distanceThreshold:
                continue
            else:
                if (src, dest) in distance:
                    continue
                else:
                    distance[(src, dest)] = length
                    distance[(dest, src)] = length
                    for neighbor in neighbors[src]:
                        heappush(heap, (length + neighbors[src][neighbor], dest, neighbor))
                    for neighbor in neighbors[dest]:
                        heappush(heap, (length + neighbors[dest][neighbor], src, neighbor))
        # print(distance)
        ans = collections.defaultdict(int)
        for i in range(n):
            for j in range(i + 1, n):
                if (i, j) in distance:
                    ans[i] += 1
                    ans[j] += 1
        # print(ans)
        min_value = min(ans.values())
        # print(min_value)
        res = 0
        for i in range(n-1,-1,-1):
            if i not in ans:
                return i
            if ans[i] == min_value:
                res = max(res, i)
        return res
        
            