# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def find_if_same(node1, node2):
            if not node1 and not node2:
                return True
            if not node1:
                return False
            if not node2:
                return False
            if node1.val == node2.val:
                return find_if_same(node1.left, node2.left) and find_if_same(node1.right, node2.right)
            else:
                return False
        # Traverse level by level to see if we can find a match
        from collections import deque
        queue = deque()
        queue.append(root)
        
        while queue:
            top = queue.popleft()
            if find_if_same(top, subRoot):
                return True
            if top:
                queue.append(top.left)
                queue.append(top.right)
        return False
            
        