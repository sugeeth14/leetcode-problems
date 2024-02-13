class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        
        def isPalindrome(s):
            l = 0
            r = len(s) - 1
            
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        for word in words:
            if isPalindrome(word):
                return word
        return ""