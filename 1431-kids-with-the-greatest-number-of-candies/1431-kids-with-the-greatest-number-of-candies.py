class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        max_value = max(candies)
        res = []
        
        for i in range(len(candies)):
            if extraCandies + candies[i] - max_value >=0:
                res.append(True)
            else:
                res.append(False)
        return res
        