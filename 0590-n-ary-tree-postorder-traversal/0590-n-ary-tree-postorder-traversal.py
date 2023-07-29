"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        
        res = []
        def postorder(node):
            for child in node.children:
                postorder(child)
            res.append(node.val)
        postorder(root)
        return res
        