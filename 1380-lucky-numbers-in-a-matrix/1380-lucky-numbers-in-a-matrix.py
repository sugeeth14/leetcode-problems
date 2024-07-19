class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        '''
        1. Go through each column and row and create max for column and min for row
        2. Once created, iterate over the matrix and compare the element.
        3. If the element is equal to the max and min add it to the res
        4. Return res at the end.
        '''
        
        res = []
        
        col = {}
        row = {} # dictionaries for row and column
        
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(rows):
            for j in range(cols):
                if j in col:
                    col[j] = max(col[j], matrix[i][j])
                else:
                    col[j] = matrix[i][j]
                
                if i in row:
                    row[i] = min(row[i], matrix[i][j])
                else:
                    row[i] = matrix[i][j]
        # after storing iterate again add populate the result
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == col[j] and matrix[i][j] == row[i]:
                    res.append(matrix[i][j])
        
        # return res at the end
        return res
        