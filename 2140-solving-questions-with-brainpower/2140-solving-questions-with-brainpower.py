class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        max_array = [0] * len(questions)
        max_value = 0
        for i in range(len(questions) -1, -1, -1):
            array_index = questions[i][1] + i + 1
            if array_index < len(questions):
                max_array[i] = questions[i][0] + max_array[array_index]
                max_value = max(max_value, max_array[i])
                max_array[i] = max_value
            else:
                max_array[i] = max(questions[i][0], max_value)
                max_value = max(max_value, max_array[i])
                max_array[i] = max_value
        return (max_value)