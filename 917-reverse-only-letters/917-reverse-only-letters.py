class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = []
        s = list(s)
        for i in range(len(s)):
            if "A" <= s[i] <= "Z" or "a" <= s[i] <="z":
                chars.append(s[i])
        chars.reverse()
        current = 0
        for i in range(len(s)):
            if "A" <= s[i] <= "Z" or "a" <= s[i] <="z":
                s[i] = chars[current]
                current +=1
        return "".join(s)
        