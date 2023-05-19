class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        
        queue = collections.deque()
        visited = {}
        
        for i in range(len(graph)):
            if len(graph[i]) != 0 and i not in visited:
                visited[i] = "Red"
                for vertex in graph[i]:
                    queue.append((vertex, "Blue"))
                # break
        
            while queue:
                top_vertex, top_color = queue.popleft()
                if top_vertex in visited:
                    # Here we don't append its children to the queue just check if the color is valid
                    if visited[top_vertex] != top_color:
                        return False
                else:
                    # It wasn't visited so mark it as visited and add its children with the opposite color
                    visited[top_vertex] = top_color
                    if top_color == "Red":
                        # All its children should be blue
                        for vertex in graph[top_vertex]:
                            queue.append((vertex, "Blue"))
                    else:
                        for vertex in graph[top_vertex]:
                            queue.append((vertex, "Red"))
        
        return True
        