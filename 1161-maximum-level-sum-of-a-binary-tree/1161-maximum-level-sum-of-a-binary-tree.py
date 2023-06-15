# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = collections.defaultdict(int)
        
        queue = collections.deque()
        queue.append((1, root))
        max_level = 1
        while queue:
            level, top = queue.popleft()
            if not top:
                continue
            ans[level] += top.val
            queue.append((level + 1, top.left))
            queue.append((level + 1, top.right))
            max_level = max(level, max_level)
        # print(ans)
        max_ans = ans[1]
        ans_level = 1
        for i in range(2, max_level + 1):
            if ans[i] > max_ans:
                max_ans = ans[i]
                ans_level = i
        return ans_level
            