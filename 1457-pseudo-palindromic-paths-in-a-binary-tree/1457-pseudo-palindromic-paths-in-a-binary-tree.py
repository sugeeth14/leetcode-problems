# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        self.dic = collections.defaultdict(int)
        
        def isPalindrome():
            count = 0
            for key in self.dic:
                if self.dic[key] %2 != 0:
                    count += 1
            return 1 if count <= 1 else 0
        
        def backtrack(node):
            if not node.left and not node.right:
                self.dic[node.val] += 1
                self.res = self.res + isPalindrome()
                self.dic[node.val] -= 1
                return
            self.dic[node.val] += 1
            if node.left:
                backtrack(node.left)
            if node.right:
                backtrack(node.right)
            self.dic[node.val] -= 1
        
        backtrack(root)
        return self.res