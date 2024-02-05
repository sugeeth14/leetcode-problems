class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = collections.defaultdict(int)
        
        for char in s:
            dic[char] += 1
        
        for i, char in enumerate(s):
            if dic[char] == 1:
                return i
        return -1
        