# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        # Always keep track of max and min on the left and right side
        
        
        self.best = float("inf")
        
        
        
        def backtrack(node):
            if not node.left and not node.right:
                return [node.val, node.val]
            else:
                if node.left and node.right:
                    left_min, left_max = backtrack(node.left)
                    right_min, right_max = backtrack(node.right)
                    current_best = min(node.val - left_max, right_min - node.val)
                    self.best = min(current_best, self.best)
                    return [left_min, right_max]
                if node.right:
                    right_min, right_max = backtrack(node.right)
                    current_best = right_min - node.val
                    self.best = min(current_best, self.best)
                    return [node.val, right_max]
                if node.left:
                    left_min, left_max = backtrack(node.left)
                    current_best = node.val - left_max
                    self.best = min(current_best, self.best)
                    return [left_min, node.val]
                    
                    
                    
        
        backtrack(root)
        return self.best
        