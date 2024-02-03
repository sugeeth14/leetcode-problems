class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        
        
        cache = {}
        
        def backtrack(i):
            if i >= len(arr):
                return 0
            
            if i in cache:
                return cache[i]
            current_max = 0
            res = 0
            for j in range(i, min((i + k), len(arr))):
                width = j - i + 1
                current_max = max(current_max, arr[j])
                product = width * current_max
                res = max(res, product + backtrack(j + 1))
            
            cache[i] = res
            return res
        
        return backtrack(0)
                
                           
        