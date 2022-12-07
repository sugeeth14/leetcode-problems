# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def find_lca(node):
            while node:
                if low <= node.val <= high:
                    return node
                if node.val < low:
                    node = node.right
                else:
                    node = node.left
            return node
            # return None

        lca = find_lca(root)
        self.sum = 0
        if not lca:
            return 0
        self.sum += lca.val
        def inorder(node):
            if not node:
                return
            else:
                inorder(node.left)
                self.sum += node.val
                inorder(node.right)
        def traverse_left(node):
            if not node:
                return
            if node.val >= low:
                self.sum += node.val
                traverse_left(node.left)
                inorder(node.right)
            elif node.val < low:
                traverse_left(node.right)
        
        def traverse_right(node):
            if not node:
                return
            if node.val > high:
                traverse_right(node.left)
            else:
                self.sum += node.val
                inorder(node.left)
                traverse_right(node.right)

        traverse_left(lca.left)
        traverse_right(lca.right)
        # print(self.sum)
        return self.sum