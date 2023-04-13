# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        from collections import deque
        queue = deque()
        queue.append((root, 1))
        max_level = 1
        while queue:
            node, level = queue.popleft()
            if node:
                max_level = max(max_level, level)
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
        return max_level
            
        