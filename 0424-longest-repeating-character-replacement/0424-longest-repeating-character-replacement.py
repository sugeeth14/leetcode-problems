class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for l in range(26):
            char = chr(65 + l)
            # print(char)
            j = 0
            count = 0
            i = 0
            ans = 0
            for j in range(len(s)):
                if s[j] != char:
                    count += 1
                while i < j and count > k:
                    if s[i] != char:
                        count -= 1
                    i += 1
                ans = max(ans, j - i + 1)
            res = max(res, ans)
        return res
            
                
            
        