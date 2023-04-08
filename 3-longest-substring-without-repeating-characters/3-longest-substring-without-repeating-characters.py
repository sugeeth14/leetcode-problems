class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        dic = {}
        longest = 0
        for r in range(len(s)):
            if s[r] not in dic or dic[s[r]] == 0:
                # No problem just add and update the longest
                longest = max(longest, r - l + 1)
                dic[s[r]] = 1
                # print("Inside if")
                # print(longest, dic)
            else:
                # Here shift the left pointer until it is 1
                dic[s[r]] += 1
                while l < r:
                    if dic[s[r]] == 1:
                        break
                    else:
                        dic[s[l]] -= 1
                        l += 1
                    
                # print("Inside else")
                # print(longest, dic, l)
                # longest = max(longest, r - l + 1)
        # longest = max(longest, r - l + 1)
        return longest
                        
                        
                        
                
                
        