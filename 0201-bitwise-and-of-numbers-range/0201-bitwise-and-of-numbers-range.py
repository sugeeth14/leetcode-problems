class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        ans = 0
        shifter = 0
        new_left = left
        new_right = right
        while new_left and new_right:
            last_left = new_left & 1
            last_right = new_right & 1
            
            
            if last_left == 1 and last_right == 1:
                if (right - left + 1) <= (1 << shifter):
                    ans = ans + (1 << shifter)
            
            shifter += 1
            new_left >>= 1
            new_right >>= 1
        return ans
                
        