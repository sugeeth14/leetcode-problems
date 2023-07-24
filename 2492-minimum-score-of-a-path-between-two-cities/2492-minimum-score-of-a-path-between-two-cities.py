class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.rank = 0
        self.min = 100002
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        node_map = {}
        for i in range(1, n+1):
            node_map[i] = Node(i)
            node_map[i].parent = node_map[i]
        
        
        
        def union(node1, node2, distance):
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2:
                parent1.min = min(parent1.min, distance)
                return
            else:
                if parent1.rank == parent2.rank:
                    parent1.rank += 1
                    parent2.parent = parent1
                    parent1.min = min(parent1.min, parent2.min, distance)
                    # parent2.min = min(parent1.min, parent2.min, distance)
                elif parent1.rank > parent2.rank:
                    parent2.parent = parent1
                    parent1.min = min(parent1.min, parent2.min, distance)
                    # parent2.min = min(parent1.min, parent2.min, distance)
                else:
                    parent1.parent = parent2
                    parent2.min = min(parent1.min, parent2.min, distance)
                return
        def find(node):
            if node.parent == node:
                return node.parent
            else:
                parent = find(node.parent)
                node.parent = parent
                return node.parent
                    
            
        for road in roads:
            union(node_map[road[0]], node_map[road[1]], road[2])
            
        return find(node_map[1]).min

            
        
        