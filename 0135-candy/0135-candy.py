class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        '''
        Algorithm
        1. Create two sequences for increasing and decreasing count
        2. Go over each of them and add the max at each index to the result.
        '''
        
        increasing = [1] * len(ratings)
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                increasing[i] = increasing[i-1] + 1
        
        decreasing = [1] * len(ratings)
        
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                decreasing[i] = decreasing[i+1] + 1
        
        # print(increasing, decreasing)
        ans = 0
        for i in range(len(increasing)):
            ans = ans + max(increasing[i], decreasing[i])
        return ans