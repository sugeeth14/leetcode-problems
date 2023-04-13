# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isMirror(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1:
                return False
            elif not node2:
                return False
            elif node1.val == node2.val:
                return isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)
            else:
                return False
        return isMirror(root.left, root.right)
        