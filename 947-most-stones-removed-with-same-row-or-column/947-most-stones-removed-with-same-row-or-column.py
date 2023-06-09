class Node:
    def __init__(self, stone):
        self.stone = stone
        self.parent = None
        self.rank = 0
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
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
                return
            else:
                if parent1.rank == parent2.rank:
                    parent1.rank += 1
                    parent2.parent = parent1
                elif parent1.rank > parent2.rank:
                    parent2.parent = parent1
                else:
                    parent1.parent = parent2
        
        #Create node maps
        node_map = {}
        for i in range(len(stones)):
            node = Node(stones[i])
            node.parent = node
            node_map[i] = node
        
        for i in range(len(stones)):
            for j in range(i+1, len(stones)):
                stone1, stone2 = stones[i], stones[j]
                
                if stone1[0] == stone2[0] or stone1[1] == stone2[1]:
                    union(node_map[i], node_map[j])
        
        parents = 0
        # print(node_map)
        
        
        for i  in range(len(stones)):
            if node_map[i].parent == node_map[i]:
                parents += 1
        
        return len(stones) - parents
        
        
        