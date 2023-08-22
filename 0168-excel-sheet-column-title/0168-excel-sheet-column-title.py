class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        

        final_string = ""
        while (columnNumber >  26):
            diff = columnNumber % 26
            if diff == 0:
                diff += 26

            final_string  = chr(int(diff) + 64) + final_string
            # print(final_string)
            columnNumber = (columnNumber - diff) / 26

        final_string = chr(int(columnNumber) + 64) + final_string

        return (final_string)


        