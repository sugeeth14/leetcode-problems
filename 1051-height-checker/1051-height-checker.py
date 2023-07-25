class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        count = 0
        
        for i, j in zip(heights, sorted(heights)):
            if i != j :
                count += 1
        return count
        