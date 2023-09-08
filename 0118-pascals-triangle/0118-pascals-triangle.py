class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        main_array = [[1], [1, 1]]
        # print(main_array)

        for i in range(2, numRows):
            main_array.append([1])
            for j in range(1, i):
                main_array[i].append(main_array[i-1][j-1] + main_array[i-1][j])
            main_array[i].append(1)

        return main_array
