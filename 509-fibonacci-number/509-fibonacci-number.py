class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        if n <= 1:
            return a if n == 0 else b
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b
            
        