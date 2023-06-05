class Node:
    def __init__(self, data):
        self.data = data
        self.rank = 0
        self.parent = None

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        
        node_map = {}
        
        
        def find(node):
            if node.parent == node:
                return node.parent
            else:
                parent = find(node.parent)
                node.parent = parent
                return node.parent
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2:
                return
            else:
                if parent1.rank == parent2.rank:
                    parent2.parent = parent1
                    parent1.rank = parent1.rank + 1
                elif parent1.rank > parent2.rank:
                    parent2.parent = parent1
                else:
                    parent1.parent = parent2
                    
        # Create nodes for each of the node in connected
        for i in range(len(isConnected)):
            node = Node(i)
            node.parent = node
            node_map[i] = node
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]:
                    union(node_map[i], node_map[j])
        ans = 0
        for i in range(len(isConnected)):
            if node_map[i].parent == node_map[i]:
                ans += 1
        return ans
        
        
        
        
        