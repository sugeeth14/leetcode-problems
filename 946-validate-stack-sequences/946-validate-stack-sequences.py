class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        ptr1 = 0
        ptr2 = 0
        
        from collections import deque
        stack = deque()
        stack.append(pushed[0])
        ptr1 += 1
        while ptr1 < len(pushed) and ptr2 < len(popped):
            if not stack:
                stack.append(pushed[ptr1])
                ptr1 += 1
            elif stack[-1] == popped[ptr2]:
                stack.pop()
                ptr2 += 1
            else:
                stack.append(pushed[ptr1])
                ptr1 += 1
        while ptr2 < len(popped):
            if not stack:
                return False
            if stack[-1] == popped[ptr2]:
                stack.pop()
                ptr2 += 1
            else:
                return False
        return True
        