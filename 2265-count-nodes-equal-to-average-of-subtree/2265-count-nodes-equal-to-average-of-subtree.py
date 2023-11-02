# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        self.res = 0
        
        def inorder(node):
            if not node:
                return (0, 0)
            else:
                left_sum, left_count = inorder(node.left)
               
                right_sum, right_count = inorder(node.right)
                
                current = left_sum + right_sum + node.val
                avg = current//(1 + left_count + right_count)
                if node.val == avg:
                    self.res += 1
                return (current, 1 + left_count + right_count)
        
        inorder(root)
        
        return self.res