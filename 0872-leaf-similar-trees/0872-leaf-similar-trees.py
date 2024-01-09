# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        '''
        Algorithm
        1. Do a inorder traversal on both the trees
        2. Whenever you encounter a leaf node add it to the list of leaves
        3. Compare two lists and return true if they are the same.
        '''
        
        self.list1 = []
        
        def inorder(node):
            if not node:
                return
            if not node.left and not node.right:
                # print(node.val)
                self.list1.append(node.val)
            if node.left:
                inorder(node.left)
            if node.right:
                inorder(node.right)
            # print(self.list1)
        
        self.list2 = []
        def inorder2(node):
            if not node:
                return
            if not node.left and not node.right:
                
                self.list2.append(node.val)
            if node.left:
                inorder2(node.left)
            if node.right:
                inorder2(node.right)
        # print(self.list1, self.list2)
        inorder(root1)
        inorder2(root2)
        # print(self.list1, self.list2)
        
        return self.list1 == self.list2
        