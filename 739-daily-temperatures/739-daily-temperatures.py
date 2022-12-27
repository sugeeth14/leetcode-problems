class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                top, index = stack.pop()
                res[index] = (i - index)
            stack.append((temperatures[i], i))
        return(res)