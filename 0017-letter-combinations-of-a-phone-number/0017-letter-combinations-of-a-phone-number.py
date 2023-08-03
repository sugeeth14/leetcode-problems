class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        result = []

        mapping = ["", "", 'abc', 'def','ghi', 'jkl','mno','pqrs','tuv','wxyz']

        length = len(digits)


        index = 0
        def combinations_recursive(current_string, index):
            if index == length:
                result.append(current_string)
                # print(result)
            else:
                for char in mapping[int(digits[index])]:
                    combinations_recursive(current_string + char, index+1)

        combinations_recursive("", index)
        return (result)



