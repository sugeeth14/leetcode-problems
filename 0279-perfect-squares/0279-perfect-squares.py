class Solution:
    def numSquares(self, n: int) -> int:
        '''
        Algorithm:
        1. Start from 1 to n
        2. Pre compute a set of squares less than n
        4. if current value in that set assign 1 to it
        5. Else find the min of values of sum of (n-x, x) where x ranges from 1 to n//2
        6. This min will be the result at a particular number i
        7. return the value at n at the end
        '''
        dic = {}
        dic[0] = 0
        squares = []
        
        for i in range(1, n + 1):
            product = i * i
            if product > n :
                break
            squares.append(product)
        for i in range(1, n + 1):
            dic[i] = n
            for square in squares:
                if i < square:
                    break
                dic[i] = min(dic[i], 1 + dic[i - square])
        return dic[n]
        