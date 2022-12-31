class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        
        res = ""
        for i in range(len(words)):
            res += words[i][::-1]
            res += " "
        return res.rstrip()