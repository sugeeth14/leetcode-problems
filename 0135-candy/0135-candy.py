class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        
        increasing = [1] * len(ratings)
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                increasing[i] = increasing[i-1] + 1
        
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                increasing[i] = max(increasing[i], increasing[i+1] + 1)
        
        return sum(increasing)
            
        