class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = rowIndex


        def get_binomial_coeffs(row):
            coeffs = [0] * (row+1)
            prev = 1
            coeffs[0] = prev
            coeffs[row] = prev
            for i in range(0, row//2):
                # print(row -i , i + 1)
                value = prev * (row - i) // (i + 1)
                coeffs[i+1] = value
                coeffs[row - i - 1] = value
                prev = value

            return coeffs






        pascal_triangle = get_binomial_coeffs(row)
        return pascal_triangle
