# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def constructTree(l, r):
            if l > r:
                return None
            elif l == r:
                return TreeNode(nums[l])
            else:
                mid = (l + r)//2
                middleNode = TreeNode(nums[mid])
                middleNode.left = constructTree(l, mid - 1)
                middleNode.right = constructTree(mid + 1, r)
                return middleNode
        return  constructTree(0, len(nums) - 1)
        # return tree
        