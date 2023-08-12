class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n <= 2:
            return [i for i in range(n)]
        
        neighbors = [set() for _ in range(n)]
        
        for edge in edges:
            neighbors[edge[0]].add(edge[1])
            neighbors[edge[1]].add(edge[0])
        
        # initial leaves are the ones which have just one neighbor
        
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)
        
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            
            new_leaves = [] # prepare for the next iteration
            
            for leaf in leaves:
                # remove the leaf and add its neighbors to the new leaves if their neighbors count is 1
                neighbor = neighbors[leaf].pop()
                neighbors[neighbor].remove(leaf)
                
                
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves
        
        
        