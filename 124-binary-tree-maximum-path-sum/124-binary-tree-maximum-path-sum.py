# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # Recursively do a post order traversal and fill in the values of sums of all the children of that node.
        dic = {}
        
        def backtrack(node):
            if node.left == None and node.right == None:
                dic[node] = node.val
                return max(node.val,0)
            else:
                left_val = 0
                right_val = 0
                if node.left:
                    left_val = backtrack(node.left)
                    # dic[node.left] = left_val
                if node.right:
                    right_val = backtrack(node.right)
                    # dic[node.right] = right_val
                dic[node] = max(left_val, 0) + max(right_val,0) + node.val
                # print(node, dic[node])
                return max(max(left_val, right_val,0) + node.val,0)
                # return dic[node]
        
        backtrack(root)
        # print(dic)
        max_value = root.val
        for key in dic:
            # print(dic[key])
            max_value = max(dic[key], max_value)
        return max_value
        