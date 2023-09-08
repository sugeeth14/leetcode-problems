class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ans = inf
        
        neighbors = collections.defaultdict(dict)
        for flight in flights:
            neighbors[flight[0]][flight[1]] = flight[2]
        # print(neighbors)
        queue = collections.deque()
        queue.append((0, 0, src))
        ans = inf
        res = {}
        while queue:
            distance, stops, node = queue.popleft()
            if node == dst:
                ans = min(ans, distance)
            else:
                if stops == k + 1:
                    continue
                else:
                    # if node in res:
                    #     if distance > res[node][0] and stops > res[node][1]:
                    #         continue
                    # else:
                    #     res[node] = [distance, stops]
                    # else:
                        # append the neighbors
                    if distance > ans:
                        continue
                    if node not in res:
                        res[node] = [distance, stops]
                    else:
                        if distance > res[node][0] and stops > res[node][1]:
                            continue
                    for neighbor in neighbors[node]:
                        queue.append((distance + neighbors[node][neighbor], stops + 1, neighbor))
        return ans if ans != inf else -1
        