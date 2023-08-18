class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        # keep track of a count of number of character in the window not equal to k
        # every time that number is 0 update the longest
        if k <= 1:
            # print("here")
            return len(s)
        
        longest = 0
        
        for i in range(len(s)):
            dic = collections.defaultdict(int)
            current = 0
            for j in range(i, len(s)):
                dic[s[j]] += 1
                if dic[s[j]] == 1:
                    current += 1
                if dic[s[j]] == k:
                    current -= 1
                
                if current == 0:
                    longest = max(longest, j - i + 1)
        return longest
                
        