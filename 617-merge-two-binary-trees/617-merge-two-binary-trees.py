# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def preorder(node1, node2):
            if not node2 and not node1:
                return None
            current_node = TreeNode()
            if node1 and node2:
                current_node.val = node1.val + node2.val
                current_node.left = preorder(node1.left, node2.left)
                current_node.right = preorder(node1.right, node2.right)
            elif node1:
                current_node.val = node1.val
                current_node.left = preorder(node1.left, None)
                current_node.right = preorder(node1.right, None)
            else:
                current_node.val = node2.val
                current_node.left = preorder(None, node2.left)
                current_node.right = preorder(None, node2.right)
            return current_node
        new_root = preorder(root1, root2)
        return new_root
        