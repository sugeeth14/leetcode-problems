class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for char in s:
            if stack:
                if char != stack[-1] and (stack[-1].upper() == char or char.upper() == stack[-1]):
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        return "".join(stack)
        