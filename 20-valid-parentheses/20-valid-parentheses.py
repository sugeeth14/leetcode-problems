class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        
        stack = deque()
        
        for char in s:
            if stack:
                if (char == ")" and stack[-1] == "(") or (char == "]" and stack[-1] == "[") or (char == "}" and stack[-1] == "{"):
                    # print(char, stack[-1])
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        if stack:
            return False
        return True
        