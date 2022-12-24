# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        if not root:
            return res
        from collections import deque
        q = deque()
        q.append((root, 0))
        while q:
            top, cur_level = q.popleft()
            if cur_level == len(res):
                res.append(top.val)
            if top.right:
                q.append((top.right, cur_level + 1))
            if top.left:
                q.append((top.left, cur_level + 1))
        return res
        