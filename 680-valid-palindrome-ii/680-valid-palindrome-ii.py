class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def checkPalindrome(current_string):
            l = 0
            r = len(current_string) - 1
            while l < r:
                if current_string[l] != current_string[r]:
                    return False
                l += 1
                r -= 1
            return True
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # We have two string choices here either not considering the character at l or not considering the character at r
                return checkPalindrome(s[l+1:r + 1]) or checkPalindrome(s[l:r])
        return True
        