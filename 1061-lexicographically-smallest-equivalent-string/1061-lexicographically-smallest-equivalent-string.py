class Node:
    def __init__(self,data):
        self.data = data
        self.parent = None
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        def union(node1, node2):
            parent1, parent2 = find(node1.parent), find(node2.parent)
            
            if parent1 == parent2:
                return
            else:
                if parent1.data <= parent2.data:
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
        
        for i in range(len(s1)):
            if s1[i] not in  node_map:
                node_map[s1[i]] = Node(s1[i])
                node_map[s1[i]].parent = node_map[s1[i]]
            if s2[i] not in node_map:
                node_map[s2[i]] = Node(s2[i])
                node_map[s2[i]].parent = node_map[s2[i]]
        
        
        
        for i in range(len(s1)):
            union(node_map[s1[i]], node_map[s2[i]])
        
        res = ""
        for i in range(len(baseStr)):
            res = res + (find(node_map[baseStr[i]]).data if baseStr[i] in node_map else baseStr[i])
        return res
        