# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        dic = collections.defaultdict(int)
        
        def backtrack(node):
            if not node:
                return
            else:
                dic[node.val] += 1
                backtrack(node.left)
                backtrack(node.right)
        backtrack(root)
        # print(dic)
        max_value = max(dic.values())
        # print(max_value)
        res = []
        for key in dic:
            if dic[key] == max_value:
                res.append(key)
        return res
        