class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2:]
        vowels = "AEIOUaeiou"
        count1 = count2 = 0
        for char in s1:
            if char in vowels:
                count1 += 1
        for char in s2:
            if char in vowels:
                count2 += 1
        return count1 == count2
            