class Node:
    def __init__(self, data):
        self.data = data
        self.rank = 0
        self.parent = None
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
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
        for eq in equations:
            if eq[1:3] == "==":
                # We must union in this case
                if eq[0] not in node_map:
                    node_map[eq[0]] = Node(eq[0])
                    node_map[eq[0]].parent = node_map[eq[0]]
                if eq[3] not in node_map:
                    node_map[eq[3]] = Node(eq[3])
                    node_map[eq[3]].parent = node_map[eq[3]]
                union(node_map[eq[0]], node_map[eq[3]])
        
        # print(node_map)
        
        for eq in equations:
            # check if the not equals belong to different clusters
            if eq[1:3] == "!=":
                if eq[0] == eq[3]:
                    return False
                elif eq[0] not in node_map or eq[3] not in node_map:
                    continue
                else:
                    parent1, parent2 = find(node_map[eq[0]]), find(node_map[eq[3]])
                    # print(parent1.data, parent2.data)
                    if parent1 == parent2:
                        return False
        return True
        