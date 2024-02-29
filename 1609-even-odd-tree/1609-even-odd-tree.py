# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque()
        odd_last = 0
        odd_level_last = -1
        even_last = 0
        even_level_last = -1
        
        queue.append((root, 0))
        while queue:
            top, level = queue.popleft()
            if level % 2 == 0:
                # check if value is odd
                if top.val % 2 == 0:
                    return False
                # check if strictly increasing
                if level == odd_level_last:
                    # should be increasing
                    if top.val <= odd_last:
                        return False
                    else:
                        # good so update odd last value
                        odd_last = top.val
                else:
                    # new level started
                    odd_level_last = level
                    odd_last = top.val
            else:
                # check if value is even
                if top.val %2 != 0:
                    return False
                # check if strictly decreasing
                if level == even_level_last:
                    # should be decreasing
                    if top.val >= even_last:
                        return False
                    else:
                        # good so update even last value
                        even_last = top.val
                else:
                    # new level started
                    even_level_last = level
                    even_last = top.val
            # append the children
            if top.left:
                queue.append((top.left, level + 1))
            if top.right:
                queue.append((top.right, level + 1))
        return True # if everything satisfies
            
        
        