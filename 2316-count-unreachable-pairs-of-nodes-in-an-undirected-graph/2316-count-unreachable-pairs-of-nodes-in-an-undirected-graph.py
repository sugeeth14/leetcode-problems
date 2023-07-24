class Node:
    def __init__(self, data):
        self.data = data
        self.count = 1 # counts the number of nodes in this cluster
        self.parent = None
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        node_map = {}
        
        for i in range(n):
            node_map[i] = Node(i)
            node_map[i].parent = node_map[i]
            
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2:
                return
            else:
                if parent1.count >= parent2.count:
                    parent1.count += parent2.count
                    parent2.parent = parent1
                else:
                    parent2.count += parent1.count
                    parent1.parent = parent2
                
        def find(node):
            if node.parent == node:
                return node.parent
            else:
                parent = find(node.parent)
                node.parent = parent
                return node.parent
            
        
        
        
        for edge in edges:
            union(node_map[edge[0]], node_map[edge[1]])
            
        ans = 0
        for i in range(n):
            if node_map[i].parent == node_map[i]:
                ans = ans + (node_map[i].count * (n - node_map[i].count))
        return ans//2
        
        