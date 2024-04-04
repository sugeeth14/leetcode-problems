class Solution:
    def maxDepth(self, s: str) -> int:
        left_brackets = 0
        
        res = 0
        for char in s:
            if char == "(":
                left_brackets += 1
                res = max(res, left_brackets)
            elif char == ")":
                left_brackets -= 1
            else:
                continue
        return res
        