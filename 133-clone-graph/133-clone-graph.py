"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        dic = {}
        
        from collections import deque
        q = deque()
        q.append(node)
        
        while q:
            top = q.popleft()
            if top.val in dic:
                continue
            dic[top.val] = []
            for neighbor in top.neighbors:
                dic[top.val].append(neighbor.val)
                q.append(neighbor)
        # print(dic)
        nodes = {}
        for i in range(len(dic)):
            nodes[i + 1] = Node(i + 1)
        for key in dic:
            current_node = nodes[key]
            for neighbor in dic[key]:
                current_node.neighbors.append(nodes[neighbor])
        return nodes[1]
            
            
        