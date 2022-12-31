class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # half_length = len(s)//2
        # for i in range(half_length):
        #     s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
        s.reverse()
        
        