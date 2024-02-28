# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        
        
        self.max_level = 0
        self.res = root.val
        def backtrack(node, level):
            if not node.left and not node.right:
                # print(node.val, level)
                # this can be potentially last level
                if level > self.max_level:
                    self.res = node.val
                    self.max_level = level
                return
            else:
                level += 1
                if node.left:
                    backtrack(node.left, level)
                if node.right:
                    backtrack(node.right, level)
                return
        
        backtrack(root, 0)
        return self.res
                