# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def preorder(node, current_max, current_min):
            if not node:
                return
            else:
                val = node.val
                self.res = max(abs(current_max - val), self.res, abs(current_min - val))
                current_max = max(val, current_max)
                current_min = min(val, current_min)
                preorder(node.left, current_max, current_min)
                preorder(node.right, current_max, current_min)
        preorder(root, root.val, root.val)
        return self.res
            
        