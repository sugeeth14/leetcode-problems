class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        Algorithm:
        1. We will maintain a stack for our purpose
        2. Whenever we encounter a number, we push into the stack
        3. When we encounter an operator, we pop from the stack the last two elements and apply the operation on them
        4. Then we push the appplied element into the stack again.
        5. At the end we return the single element in the stack as the result.
        '''
        stack = []
        
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                # we have to perform the operation
                top1 = stack.pop()
                top2 = stack.pop()
                if token == "+":
                    stack.append(top1 + top2)
                elif token == "-":
                    stack.append(top2 - top1)
                elif token == "*":
                    stack.append(top1 * top2)
                else:
                    stack.append(int(top2/top1))
            else:
                stack.append(int(token))
            # print(stack)
        return stack[0]
                
        