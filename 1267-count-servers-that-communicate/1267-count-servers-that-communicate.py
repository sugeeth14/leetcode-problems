class Node:
    def __init__(self, identifier):
        self.id = identifier
        self.count = 0 # Every row and column has 0 servers at start
        self.parent = None
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # Algorithm
        # 1. Each row and column is a node in our graph
        # 2. Whenever there is a 1 we can union the row and the column
        # 3. The resulting node will have a count which combines the count of the row and the column
        # 4. We can then add one to the combined parent count.
        # 5. At the end iterate over the rows and the columns and see if the count is > 2 and the node is the parent
        # 6. If so add to the res
        # Rows can go from 0 ->m and cols can go form m->m + n
        m = len(grid)
        n = len(grid[0])
        
        node_map = {}
        
        for i in range(m):
            node_map[i] = Node(i)
            node_map[i].parent = node_map[i]
        for i in range(m, m + n):
            node_map[i] = Node(i)
            node_map[i].parent = node_map[i]
        
        # print(node_map)
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2:
                return parent1
            else:
                if parent1.count >= parent2.count:
                    parent2.parent = parent1
                    parent1.count += parent2.count
                    return parent1
                else:
                    parent1.parent = parent2
                    parent2.count += parent1.count
                    return parent2
        
        def find(node):
            if node.parent == node:
                return node.parent
            else:
                parent = find(node.parent)
                node.parent = parent
                return node.parent
                    
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # We must union the row and the column and get the parent
                    parent = union(node_map[i], node_map[j + m])
                    parent.count += 1
        
        # iterate over the nodes and check if they are parents and add to the final result
        res = 0
        for i in range(m + n):
            if node_map[i].parent == node_map[i]:
                if node_map[i].count >= 2:
                    res += node_map[i].count
        return res
        