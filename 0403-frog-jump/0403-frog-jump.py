class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        target = stones[-1]
        
        stones_set = set(stones)
        
        
        
        cache = {}
        def backtrack(current, k):
            # print(current, k , cache)
            if k == 0:
                return False
            if (current, k) in cache:
                return cache[(current, k)]
            if current not in stones_set:
                return False
            else:
                if current == target:
                    return True
                elif current > target:
                    return False
                else:
                    ans = backtrack(current + k, k) or backtrack(current + k - 1,k - 1) or backtrack(current + k + 1, k + 1)
                    cache[(current, k)] = ans
                    return ans
        
        return backtrack(1, 1)
        
                
        