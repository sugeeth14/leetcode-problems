class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        res = 0
        
        stack = []
        mod = 1000000007
        
        for i, n in enumerate(arr):
            
            while stack and n < stack[-1][1]:
                j, m = stack.pop()
                
                left_product = j - stack[-1][0] if stack else j + 1
                
                right_product = i - j
                
                res = (res + m * left_product * right_product) % mod
            stack.append((i, n))
        
        for i in range(len(stack)):
            top, val = stack[i]
            
            left_product = top - stack[i-1][0] if i > 0 else top + 1
            
            right_product = len(arr) - top
            res = res + (val * left_product * right_product) % mod
        
        
        
        
        
        
        return res % mod
        