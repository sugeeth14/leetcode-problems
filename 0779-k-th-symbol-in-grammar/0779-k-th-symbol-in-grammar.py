class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        # so there are two choices either move to right or to the left
        
        total_elements = 1  << (n-1)
        current = 0
        while total_elements != 1:
            total_elements >>= 1
            if k <= total_elements:
                current = current
            else:
                current = (current + 1) % 2
                k -= total_elements
        return current
            
        