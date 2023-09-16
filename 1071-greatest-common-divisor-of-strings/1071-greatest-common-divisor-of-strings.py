class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        min_length = min(len(str1), len(str2))
        
        for i in range(min_length, 0, -1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                temp_string = (str2[:i] * (len(str2)//i))
                temp_string2 = (str2[:i] * (len(str1)//i))
                
                if temp_string == str2 and temp_string2 == str1:
                    return str2[:i]
        return ""
        