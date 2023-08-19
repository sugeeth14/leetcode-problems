class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        next_str = ""
        
        for i in range(len(str1)):
            if str1[i] == "z":
                next_str += "a"
            else:
                next_str = next_str + chr(1 + ord(str1[i]))
        # print(next_str)
        i = 0
        j = 0
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j] or next_str[i] == str2[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j == len(str2) 
                
        
        