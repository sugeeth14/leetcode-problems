class Solution:
    def minOperations(self, s: str) -> int:
        # you either make it 0101....
        # or 1010...
        ans1 = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "1":
                    ans1 += 1
            else:
                if s[i] == "0":
                    ans1 += 1
        ans2 = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "0":
                    ans2 += 1
            else:
                if s[i] == "1":
                    ans2 += 1
        
        return min(ans1, ans2)
        