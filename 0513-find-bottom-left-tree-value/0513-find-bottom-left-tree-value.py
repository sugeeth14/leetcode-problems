# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque()
        self.res = root.val
        self.best_level = 0
        queue.append((root, 0))
        
        while queue:
            top, level = queue.popleft()
            if level > self.best_level:
                self.best_level = level
                self.res = top.val
            # push the children
            if top.left:
                queue.append((top.left, level + 1))
            if top.right:
                queue.append((top.right, level + 1))
        
        return self.res
        