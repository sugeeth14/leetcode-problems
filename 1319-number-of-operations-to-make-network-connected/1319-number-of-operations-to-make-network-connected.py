class Node:
    def __init__(self, data):
        self.data = data
        self.rank = 0
        self.parent = None
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # Algorithm
        # 1. Find the count of the wires which make redundant connections
        # 2. Union based on the connections and keep track of this count
        # 3. At the end, count the total number of cluster, the number of wires needed would be clusters - 1
        # 4. If the count >= clusters -1 return clusters - 1 else return -1
        
        node_map = {}
        for i in range(n):
            node_map[i] = Node(i)
            node_map[i].parent = node_map[i]
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2: # Redundant connection as they already part of a cluster
                return True
            else:
                if parent1.rank == parent2.rank:
                    parent1.rank += 1
                    parent2.parent = parent1
                elif parent1.rank > parent2.rank:
                    parent2.parent = parent1
                else:
                    parent1.parent = parent2
                return False
        
        def find(node):
            if node.parent == node:
                return node.parent
            else:
                parent = find(node.parent)
                node.parent = parent
                return node.parent
            
        count = 0
        for connection in connections:
            if union(node_map[connection[0]], node_map[connection[1]]):
                # It is a redundant connection, increment the count
                count += 1
        # count the clusters
        clusters = 0
        for i in range(n):
            if node_map[i].parent == node_map[i]:
                clusters += 1
        if clusters - 1 > count:
            return - 1
        return clusters - 1
            
        
        
        