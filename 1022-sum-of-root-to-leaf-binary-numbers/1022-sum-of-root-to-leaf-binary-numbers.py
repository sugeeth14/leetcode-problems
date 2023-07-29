# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        
        self.total = 0
        
        def backtrack(node, current_sum):
            if not node.left and not node.right:
                current_sum += node.val
                self.total += current_sum
                return
            else:
                current_sum += node.val
                current_sum <<= 1
                if node.left:
                    backtrack(node.left, current_sum)
                if node.right:
                    backtrack(node.right, current_sum)
        
        
        backtrack(root, 0)
        return self.total
                
                
                
        