# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def inorder(node, res):
            if not node:
                res.append(None)
                return res
            else:
                
                res.append(node.val)
                if node.left or node.right:
                    res = inorder(node.left, res)
                    res = inorder(node.right, res)
                return res
        
        res1 = inorder(p, [])
        res2 = inorder(q, [])
        # print(res1, res2)
        return res1 == res2
        