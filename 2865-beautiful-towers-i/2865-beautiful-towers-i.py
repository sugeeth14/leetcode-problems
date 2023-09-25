class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        # We will try an O(n^2) algorithm
        res = 0
        for i in range(len(maxHeights)):
            # currently i index is the peak of the mountain
            current = 0
            current_max = maxHeights[i]
            for j in range(i-1,-1,-1):
                current_max = min(maxHeights[j], current_max)
                current += current_max
            current_max = maxHeights[i]
            for j in range(i+1, len(maxHeights)):
                current_max = min(maxHeights[j], current_max)
                current += current_max
                # print(current)
            # print(maxHeights[i], current)
            res = max(res, current + maxHeights[i])
        return res
                
        