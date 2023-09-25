class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if t[i] != s[i]:
                return t[i]
        return t[len(s)]
        