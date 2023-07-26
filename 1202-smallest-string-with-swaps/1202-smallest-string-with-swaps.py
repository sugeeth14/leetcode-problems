class Node:
    def __init__(self, data):
        self.data = data
        self.rank = 0
        self.parent = None
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        
        
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
        for i in range(len(s)):
            node_map[i] = Node(i)
            node_map[i].parent = node_map[i]
        
        for pair in pairs:
            union(node_map[pair[0]], node_map[pair[1]])
        
        dic = collections.defaultdict(list)
        for i in range(len(s)):
            parent = find(node_map[i])
            dic[parent].append(s[i])
            
        res = ""
        for key in dic:
            dic[key].sort(reverse=True)
        for i in range(len(s)):
            parent = find(node_map[i])
            res = res + dic[parent][-1]
            dic[parent].pop()
        return res
        