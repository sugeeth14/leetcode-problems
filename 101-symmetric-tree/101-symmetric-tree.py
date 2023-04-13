# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        levels = {}
        
        from collections import deque
        queue = deque()
        
        queue.append((root, 0))
        while queue:
            top, level = queue.popleft()
            if level in levels:
                levels[level].append(top)
            else:
                levels[level] = [top]
            if top:
                queue.append((top.left, level+ 1))
                queue.append((top.right, level + 1))
        for key in levels:
            if key != 0:
                # Check if the level forms a palindrome
                l = 0
                r = len(levels[key]) - 1
                while l < r:
                    if not levels[key][l] and not levels[key][r]:
                        pass
                    elif not levels[key][l]:
                        return False
                    elif not levels[key][r]:
                        return False
                    elif levels[key][l].val != levels[key][r].val:
                        return False
                    l += 1
                    r -= 1
        return True
        
        
        