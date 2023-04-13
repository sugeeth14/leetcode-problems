# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def isBinary(node):
            if not node.left and not node.right:
                return (True, node.val, node.val)
            elif node.left and node.right:
                leftBinary, leftMax, leftMin = isBinary(node.left)
                rightBinary, rightMax, rightMin = isBinary(node.right)
                if leftBinary and rightBinary and leftMax < node.val < rightMin:
                    return (True, rightMax, leftMin)
                else:
                    return (False, -1, -1)
            elif node.left:
                leftBinary, leftMax, leftMin = isBinary(node.left)
                if leftBinary and leftMax < node.val:
                    return (True, node.val, leftMin)
                else:
                    return (False, -1, -1)
            elif node.right:
                rightBinary, rightMax, rightMin = isBinary(node.right)
                if rightBinary and rightMin > node.val:
                    return (True, rightMax, node.val)
                else:
                    return (False, -1, -1)
                
        return isBinary(root)[0]
                    
                
        