class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # First find the row then find the column
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows - 1
        row = -1
        while l <= r:
            mid = (l + r)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                r = mid - 1
        if row == -1:
            return False
        l = 0
        r = cols - 1
        while l <= r:
            mid = (l + r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
        