class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]
        
        l = 0
        r = len(letters) - 1
        ans = float("inf")
        while l <= r:
            mid = (l + r)//2
            if letters[mid] > target:
                ans = min(mid, ans)
                r = mid - 1
            else:
                l = mid + 1
        return letters[ans]
                
        