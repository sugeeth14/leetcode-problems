class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        dic1 = collections.defaultdict(int)
        
        dic2 = collections.defaultdict(int)
        
        
        for char1, char2 in zip(s, t):
            dic1[char1] += 1
            dic2[char2] += 1
        
        
        ans = 0
        for i in range(97, 97 + 27):
            character = chr(i)
            ans = ans + abs(dic1[character] - dic2[character])
        return ans // 2
        