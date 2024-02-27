# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        Algorithm:
        1. At every node we calculate the left length and right length
        2. We return the best of two + 1 to the top
        3. While returning we can also compute the best res as left + right + 1 and update the best res
        4. Return the best res at the end.
        '''
        
        self.res = 0
        
        def backtrack(node):
            if not node:
                return 0
            
            left = backtrack(node.left)
            right = backtrack(node.right)
            self.res = max(self.res, left + right + 1)
            
            return max(left, right) + 1
        
        backtrack(root)
        return self.res - 1
        