# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque()
        queue.append((root, 0))
        res = []
        
        while queue:
            top, level = queue.popleft()
            if level == len(res):
                res.append([top.val])
            else:
                res[-1].append(top.val)
            if top.left:
                queue.append((top.left, level + 1))
            if top.right:
                queue.append((top.right, level + 1))
        return res
        