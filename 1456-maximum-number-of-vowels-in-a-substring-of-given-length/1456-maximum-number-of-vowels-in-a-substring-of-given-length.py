class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        for i in range(k):
            if s[i] in "aeiou":
                ans += 1
        if ans == k:
            return ans
        res = ans
        for i in range(k, len(s)):
            if s[i] in "aeiou":
                ans += 1
            if s[i-k] in "aeiou":
                ans -= 1
            res = max(ans, res)
            if res == k:
                return k
        return res
        
        