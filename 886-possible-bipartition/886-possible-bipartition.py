class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        edges = [[1] * n for _ in range(n)]
        for i in range(len(dislikes)):
            x, y = dislikes[i][0], dislikes[i][1]
            edges[x-1][y-1] = 0
            edges[y-1][x-1] = 0
        # print(edges)
        visited = {}
        queue = collections.deque()
        for j in range(len(edges)):
            if j in visited:
                continue
            
            queue.append((j, 1))
            visited[j] = 1
            while queue:
                node, group = queue.popleft()
                child_group = group % 2 + 1
                for i in range(len(edges[node])):
                    if edges[node][i] == 0:
                        if i not in visited:
                            visited[i] = child_group
                            queue.append((i, child_group))
                        else:
                            if visited[i] != child_group:
                                return False

        return True
            
                
            
        
        