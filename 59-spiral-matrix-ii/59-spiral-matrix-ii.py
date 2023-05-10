class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:


        result = [[0] * n for _ in range(n)]

        left, right = 0, n
        top, bottom = 0, n
        value = 0
        while left < right and top < bottom:

            for i in range(left, right):
                value += 1
                result[top][i] = value
            top += 1
            for i in range(top, bottom):
                value += 1
                result[i][right - 1] = value
            right -= 1
            for i in range(right - 1, left - 1, -1):
                value += 1
                result[bottom - 1][i] = value
            bottom -= 1
            for i in range(bottom - 1, top - 1, -1):
                value += 1
                result[i][left] = value
            left += 1


        return (result)