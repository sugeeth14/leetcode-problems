# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        dic = {}
        
        def backtrack(node, level):
            if not node:
                return
            else:
                if level in dic:
                    dic[level] = max(dic[level], node.val)
                else:
                    dic[level] = node.val
                backtrack(node.left, level + 1)
                backtrack(node.right, level + 1)
        
        backtrack(root, 0)
        res = []
        i = 0
        while i in dic:
            res.append(dic[i])
            i += 1
        return res
            
        