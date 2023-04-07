# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        from collections import deque
        queue = deque()
        queue.append(root)
        while queue:
            top = queue.pop()
            if top:
                top.left, top.right = top.right, top.left
                queue.append(top.left)
                queue.append(top.right)
        return root