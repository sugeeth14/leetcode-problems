class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            new_diff = arr[i] - arr[i-1]
            if new_diff != diff:
                return False
        return True
        