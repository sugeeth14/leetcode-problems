# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        
        dic = {}
        def backtrack(node):
            if not node:
                return False
            if k - node.val in dic:
                return True
            else:
                dic[node.val] = True
                return backtrack(node.left) or backtrack(node.right)
        
        return backtrack(root)