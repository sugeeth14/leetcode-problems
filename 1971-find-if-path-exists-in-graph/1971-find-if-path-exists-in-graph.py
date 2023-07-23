class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.rank = 0
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Algorithm
        # 1. We do union based on the edges between nodes in the edges
        # 2. The we do find on source and destination.
        # 3. If they belong to the same parent there exists a path or else no
        
        node_map = {}
        for i in range(n):
            node_map[i] = Node(i)
            node_map[i].parent = node_map[i]
        # print(node_map)
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2:
                return
            
            if parent1.rank == parent2.rank:
                parent1.rank += 1
                parent2.parent = parent1
            elif parent1.rank > parent2.rank:
                parent2.parent = parent1
            else:
                parent1.parent = parent2
        
        def find(node):
            if node.parent == node:
                return node.parent
            else:
                parent = find(node.parent)
                node.parent = parent
                return node.parent
        
        # We go over edges and do a union
        for edge in edges:
            union(node_map[edge[0]], node_map[edge[1]])
        
        source_parent = find(node_map[source])
        destination_parent = find(node_map[destination])
        
        return source_parent == destination_parent
        
        