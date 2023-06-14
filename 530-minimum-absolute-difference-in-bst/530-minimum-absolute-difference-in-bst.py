# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        nodes = []
        
        def traverse(node):
            if not node:
                return
            # if node.left:
            traverse(node.left)
            nodes.append(node.val)
            traverse(node.right)
        
        traverse(root)
        # print(nodes)
        # nodes.sort()
        
        min_diff = nodes[1] - nodes[0]
        for i in range(2, len(nodes)):
            min_diff = min(min_diff, nodes[i] - nodes[i-1])
        return min_diff
        