class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        if self.stack2:
            res = self.stack2.pop()
            return res
        else:
            while self.stack1:
                top = self.stack1.pop()
                self.stack2.append(top)
            res = self.stack2.pop()
            return res
            
        

    def peek(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        else:
            while self.stack1:
                top = self.stack1.pop()
                self.stack2.append(top)
            return self.stack2[-1]
        

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()