class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        combined = []
        for i in range(len(score)):
            combined.append([score[i], i])
        combined.sort(reverse=True)
        # print(combined)
        res = [""] * len(score)
        
        for i in range(min(3, len(combined))):
            _, index = combined[i]
            if i == 0:
                res[index] = "Gold Medal"
            elif i == 1:
                res[index] = "Silver Medal"
            else:
                res[index] = "Bronze Medal"
        for i in range(3, len(combined)):
            value, index = combined[i]
            res[index] = str(i+1)
        return res
            
        