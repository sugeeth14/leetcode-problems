class Node:
    def __init__(self, data):
        self.data = data
        self.rank = 0
        self.parent = None
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
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
        
        def find(node):
            if node.parent == node:
                return node.parent
            else:
                parent = find(node.parent)
                node.parent = parent
                return node.parent
        
        node_map = {}
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                node_map[(i, j)] = Node((i, j))
                node_map[(i, j)].parent = node_map[(i, j)]
        
        for i in range(rows):
            for j in range(cols):
                parent1 = None
                parent2 = None
                if i -1 >=0 and grid[i-1][j] == grid[i][j]:
                    parent1 = find(node_map[(i-1,j)])
                
                if j - 1 >=0 and grid[i][j-1] == grid[i][j]:
                    parent2 = find(node_map[(i, j -1)])
                
                if parent1 and parent2 and parent1 == parent2:
                    return True
                if parent1:
                    union(node_map[(i-1,j)],node_map[(i,j)])
                if parent2:
                    union(node_map[(i,j-1)], node_map[(i,j)])
        return False
        