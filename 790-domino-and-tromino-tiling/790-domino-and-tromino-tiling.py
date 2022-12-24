class Solution:
    def numTilings(self, n: int) -> int:
        
        cache = {}
        
        def backtrack(index):
            if index in cache:
                return cache[index]
            if index > n:
                return 0
            if index == n:
                return 1
            else:
                sum1 = backtrack(index + 1)
            
                sum2 = backtrack(index + 2)
                # cache[index] = sum1 + sum2 + sum3*2

                cache[index] = sum1 + sum2
                for i in range(3, n+1):
                    cache[index] += (backtrack(index + i) * 2)
                return cache[index]
                # return cache[index]
        return backtrack(0)%(1000000007)
            
        