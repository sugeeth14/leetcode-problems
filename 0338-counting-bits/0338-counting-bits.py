class Solution:
    def countBits(self, n: int) -> List[int]:


        result = [0, 1]
        last_power = 1
        for i in range(2, n + 1):
            if i & (i-1) == 0:
                result.append(1)
                last_power = i
            else:
                diff = i - last_power
                result.append(1 + result[diff])

        return (result[:n+1])

        