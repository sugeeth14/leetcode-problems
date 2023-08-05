# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        cache = {}
        def helper(first, last):
            if (first, last) in cache:
                return cache[(first,last)]
            if first > last:
                return [None]
            trees = []
            
            for root in range(first, last+1):
                for left in helper(first, root - 1):
                    for right in helper(root + 1, last):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)
            cache[(first,last)] = trees
            return trees
        return helper(1,n)
        