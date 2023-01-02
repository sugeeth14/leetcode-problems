# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Every time from leaf there are two choices to return itself or to return it by adding to each of its children individually.
        if not root:
            return 0
        
        self.count = 0
        def backtrack(node):
            if not node.left and not node.right:
                # Doesn't have both left and right
                # just return it as a single sum
                if node.val == targetSum:
                    self.count += 1
                return [node.val]
            # right_sums = []
            # left_sums = []
            res = [node.val]
            if node.val == targetSum:
                self.count += 1
            if node.right:
                # Has only right child so backtrack to right and add the value to each of the right values.
                right_sums = backtrack(node.right)

                for right_sum in right_sums:
                    val = right_sum + node.val
                    if val == targetSum:
                        self.count += 1
                    res.append(val)
            if node.left:
                left_sums = backtrack(node.left)
                for left_sum in left_sums:
                    val = left_sum + node.val
                    if val == targetSum:
                        self.count += 1
                    res.append(val)
            return res
        backtrack(root)
        return self.count
                    
        