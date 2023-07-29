class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        res = []
        
        def backtrack(value):
            if value > n:
                return
            else:
                res.append(value)
                multiple = value * 10
                for i in range(10):
                    backtrack(multiple + i)
        
        for i in range(1, 10):
            backtrack(i)
        return res
                
                    
        