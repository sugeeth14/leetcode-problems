# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # For every node maintain the left side zig zag max and the right side zig zag max and recursively build from bottom to top
        
        self.max_value = 0
        def build(node):
            if not node:
                return [0, 0]
            left_lengths = [0, 0]
            right_lengths = [0, 0]
            if node.left:
                left_lengths = build(node.left)
            if node.right:
                right_lengths = build(node.right)
            
            res = [left_lengths[1] + 1, right_lengths[0] + 1]
            self.max_value = max(max(res), self.max_value)
            return res
        build(root)
        return self.max_value - 1
                
        