# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        self.res1 = []
        
        def inorder(node):
            if not node:
                return
            if node.left or node.right:
                inorder(node.left)
                # self.res1.append(node.val)
                inorder(node.right)
            else:
                self.res1.append(node.val)
        
        self.res2 = []
        def inorder2(node):
            if not node:
                return
            if node.left or node.right:
                inorder2(node.left)
                # self.res2.append(node.val)
                inorder2(node.right)
            else:
                self.res2.append(node.val)
        
        inorder(root1)
        inorder2(root2)
        # print(self.res1)
        # print(self.res2)
        return self.res1 == self.res2
        