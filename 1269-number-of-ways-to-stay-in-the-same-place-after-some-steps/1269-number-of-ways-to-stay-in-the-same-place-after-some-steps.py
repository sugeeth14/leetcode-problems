class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        cache = {}
        mod = 1000000007
        
        def backtrack(current, index):
            if (current, index) in cache:
                return cache[(current, index)]
            elif current == 0:
                if index == 0:
                    return 1
                else:
                    return 0
            if index > current:
                return 0
            if index >= arrLen:
                return 0
            if index < 0:
                return 0
            # we have three choices
            # move left
            val1 = backtrack(current - 1, index - 1) % mod
            # move right
            
            val2 = backtrack(current -1, index + 1) % mod
            # stay
            val3 = backtrack(current-1, index) % mod
            
            cache[(current, index)] = ((val1 + val2) % mod + val3) % mod
            return cache[(current, index)]
        return backtrack(steps, 0) % mod