# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        self.val = root.val
        
        def backtrack(node):
            if not node:
                return True
            else:
                if node.val != self.val:
                    return False
                return backtrack(node.left) and backtrack(node.right)
        
        return backtrack(root)
                
        