class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        y = 0
        n = 0
        
        ans = 0
        max_diff=0
        
        for i in range(len(customers)):
            if y > n and y -n > max_diff:
                ans = i
                max_diff = y - n
            if customers[i] == "Y":
                y += 1
            else:
                n += 1
        if y > n and y - n > max_diff:
                ans = i + 1
                max_diff = y - n
        return ans
                
        
        