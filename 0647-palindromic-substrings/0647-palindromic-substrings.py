class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        Algorithm:
        1. Start with each element in the middle
        2. Keep expanding until reached boundaries or if any element on the left and right are not equal
        3. Repeat this considering each element in the middle. 
        4. Now go over each two elements and do the same expanding and keep the count
        5. Return the count at the end.
        '''
        
        count = 0
        
        for i in range(len(s)):
            left = i
            right = i
            
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break
        
        for i in range(len(s) - 1):
            j = i + 1
            
            left = i
            right = j
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break
        return count
        