class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        remaining = (len(rolls) + n) * mean
        
        remaining -= sum(rolls)
        if remaining < n:
            return []
        ans = [1] * n
        remaining -= n
        if remaining == 0:
            return ans
        else:
            if remaining > 5 * n:
                return []
            else:
                for i in range(len(ans)):
                    if remaining < 5:
                        ans[i] += remaining
                        break
                    else:
                        ans[i] += 5
                        remaining -= 5
        return ans
        
        