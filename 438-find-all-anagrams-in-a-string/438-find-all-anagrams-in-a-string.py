class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        p_array = [0] * 26
        window_array = [0] * 26
        for char in p:
            p_array[ord(char) - ord('a')] += 1
        
        for i in range(len(p)):
            window_array[ord(s[i]) - ord('a')] += 1
        res = []
        if window_array == p_array:
            res.append(0)
        for i in range(len(p), len(s)):
            window_array[ord(s[i]) - ord('a')] += 1
            window_array[ord(s[i-len(p)]) - ord('a')] -= 1
            if window_array == p_array:
                res.append(i - len(p) + 1)
        return(res)
            
        
        
        