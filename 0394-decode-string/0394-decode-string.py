class Solution:
    def decodeString(self, s: str) -> str:
        
        
        stack = collections.deque()
        
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                # print(stack)
                current = ""
                while stack[-1] != "[":
                    current = stack.pop() + current
                
                stack.pop()
                # print(current)
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                # print(num)
                new_string = int(num) * current
                
                stack.append(new_string)
        return "".join(stack)
                
        