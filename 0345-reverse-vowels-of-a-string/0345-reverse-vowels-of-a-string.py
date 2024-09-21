class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                vowels.append(s[i])
        
        vowels = vowels[::-1]
        # print(vowels)
        res = []
        last_index = 0
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                res.append(vowels[last_index])
                last_index += 1
            else:
                res.append(s[i])
        return "".join(res)
        