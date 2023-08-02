# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # At every node keep the best value with and without it and finally backtrack to the root to return the max of the root's result
        
        def backtrack(node):
            if not node:
                return [0, 0]
            else:
                left = backtrack(node.left)
                right = backtrack(node.right)
                
                
                # to get best without we must take best with from children
                without_node = max(left[1] + right[1], left[0] + right[0], left[1] + right[0], left[0] + right[1])
                with_node = node.val + left[0] + right[0]
                # print(node.val, without_node, with_node)
                
                return [without_node, with_node]
        
        res = backtrack(root)
        return max(res)
        