class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        
        res = [1] * len(pairs)
        for i in range(len(pairs)):
            for j in range(i-1,-1,-1):
                if pairs[j][1] < pairs[i][0]:
                    res[i] = res[j]+1
                    break
        return max(res)
        