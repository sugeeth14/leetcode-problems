class Solution:
    def numDecodings(self, s: str) -> int:







        if s[0] == "0":
            return 0
        else:
            isolated, combined = 1, 0

        for i in range(1, len(s)):
            if s[i] == "0":
                temp = isolated
                isolated = 0
                combined = temp
                if s[i-1] > "2":
                    combined = 0
            elif s[i - 1] == "2" and (s[i] == "7" or s[i] == "8" or s[i] == "9"):
                isolated = isolated + combined
                combined = 0
            elif s[i - 1] > "2":
                isolated = isolated + combined
                combined = 0
            else:
                temp = isolated
                isolated = isolated + combined
                combined = temp

        return (isolated + combined)
    



