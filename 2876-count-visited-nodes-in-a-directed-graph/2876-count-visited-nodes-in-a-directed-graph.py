class Node:
    def __init__(self, data):
        self.data = data
        self.rank = 1
        self.parent = None
class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2:
                return
            else:
                # we must union
                if parent1.rank >= parent2.rank:
                    parent2.parent = parent1
                    parent1.rank += parent2.rank
                else:
                    parent1.parent = parent2
                    parent2.rank += parent1.rank
        def find(node):
            if node.parent == node:
                return node.parent
            else:
                parent = find(node.parent)
                node.parent = parent
                return node.parent
        
        node_map = {}
        for i in range(len(edges)):
            node = Node(i)
            node.parent = node
            node_map[i] = node
        
        for i in range(len(edges)):
            union(node_map[i], node_map[edges[i]])
        
        def find_sheep(node):
            visited = set()
            current = node.data
            visited.add(current)
            while True:
                next_vertex = edges[current]
                if next_vertex in visited:
                    return next_vertex
                else:
                    current = next_vertex
                    visited.add(next_vertex)
        
        sheeps = {}
        for i in range(len(edges)):
            parent = find(node_map[i])
            if parent not in sheeps:
                sheep = find_sheep(parent)
                sheeps[parent] = sheep
        
        def get_cluster(node):
            # get all the elements of the cycle
            sheep = sheeps[node]
            cluster = set()
            cluster.add(sheep)
            while True:
                next_vertex = edges[sheep]
                if next_vertex not in cluster:
                    cluster.add(next_vertex)
                    sheep = next_vertex
                else:
                    break
            return cluster
        clusters = {}
        for i in range(len(edges)):
            parent = find(node_map[i])
            if parent not in clusters:
                clusters[parent] = get_cluster(parent)
        # print(clusters)
        res = []
        for i in range(len(edges)):
            ans = 0
            parent = find(node_map[i])
            parent_cluster = clusters[parent]
            current = i
            while current not in parent_cluster:
                current = edges[current]
                ans += 1
            res.append(ans + len(parent_cluster))
        return res
            
        