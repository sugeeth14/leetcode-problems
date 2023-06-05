class Node:
    def __init__(self, data):
        self.data = data
        self.rank = 0
        self.parent = None
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        
        # The moment the number of connected components becomes 1 is when the edge is unnecessary
        
        node_map = {}
        
        def find(node):
            
            if node.parent == node:
                return node
            else:
                parent = find(node.parent)
                node.parent = parent
                return node.parent
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            
            if parent1 == parent2:
                return False
            else:
                if parent1.rank == parent2.rank:
                    parent1.rank += 1
                    parent2.parent = parent1
                elif parent1.rank > parent2.rank:
                    parent2.parent = parent1
                else:
                    parent1.parent = parent2
                return True
        
        for i in range(len(edges)):
            node = Node(i + 1)
            node.parent = node
            node_map[i+1] = node
        
        # connected_components = len(edges)
        
        for i in range(len(edges)):
            edge = edges[i]
            can_union = union(node_map[edge[0]], node_map[edge[1]])
            if not can_union:
                return edge
        # print
            
            
        