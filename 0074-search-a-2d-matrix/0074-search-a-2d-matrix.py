class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2
            if mid == r:
                break
            if matrix[mid][0] <= target and matrix[mid + 1][0] > target:
                break
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1
        search_row = mid
        l, r = 0, len(matrix[0]) - 1
        is_found = False
        while l <= r:
            mid = (l + r) // 2
            if matrix[search_row][mid] == target:
                is_found = True
                break
            elif matrix[search_row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return (is_found)

