class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        
        stack = []
        
        for i in range(len(s)):
            if s[i] == "(":
                stack.append([i, "("])
            elif s[i] == ")":
                if stack and stack[-1][1] == "(":
                    stack.pop()
                else:
                    stack.append([i, ")"])
        
        current = 0
        res = ""
        # print(stack)
        
        for i in range(len(s)):
            if current < len(stack) and stack[current][0] == i:
                current += 1
                continue
            else:
                res += s[i]
        return res