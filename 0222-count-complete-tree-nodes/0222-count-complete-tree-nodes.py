# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        
        
        def backtrack(node):
            if not node:
                return 0
            lh = find_left(node)
            rh = find_right(node)
            if lh == rh:
                return (1 << lh) - 1
            else:
                return 1 + backtrack(node.left) + backtrack(node.right)
        
        def find_left(node):
            level = 1
            while node.left:
                level += 1
                node = node.left
            return level
        def find_right(node):
            level = 1
            while node.right:
                level += 1
                node = node.right
            return level
        
        return backtrack(root)