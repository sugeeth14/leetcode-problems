class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        gcd = math.gcd(len(str1), len(str2))
        # print(gcd)
        
        temp1 = str1[:gcd] * (len(str1)//gcd)
        temp2 = str1[:gcd] * (len(str2)//gcd)
        
        if temp1 == str1 and temp2 == str2:
            return str1[:gcd]
        return ""
        