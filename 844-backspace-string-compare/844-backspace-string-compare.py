class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        from collections import deque
        stack1 = deque()
        for char in s:
            if char == "#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(char)
        stack2 = deque()
        for char in t:
            if char == "#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(char)
        # print(stack1, stack2)
        return stack1 == stack2
        