# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def get_width(str1, str2):
            # print(str1, str2)
            res = 0
            for i in range(len(str1)):
                res = res << 1
                if str1[i] == str2[i]:
                    continue
                else:
                    if str2[i] == "1":
                        res += 1
                    else:
                        res -= 1
            # print(res)
            return res + 1
                
        
        queue = collections.deque()
        
        queue.append((root,0,  "1"))
        
        max_width = 1
        current = 0
        while queue:
            _, level, _ = queue[0]
            if level != current:
                max_width = max(get_width(queue[0][2], queue[-1][2]), max_width)
                current = level
            node, level, rep = queue.popleft()
            
            if node.left:
                queue.append((node.left, level + 1, rep + "0"))
            if node.right:
                queue.append((node.right, level + 1, rep + "1"))
            # print(queue)
            # print(max_width)
        return max_width
                
            
            
        