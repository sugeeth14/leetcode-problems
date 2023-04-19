class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        min_number = float("infinity")
        while l < r:
            mid = (l + r)//2
            if nums[mid] < nums[r]:
                # You must go to left but before that update min
                min_number = min(min_number, nums[mid])
                r = mid - 1
            else:
                min_number = min(min_number, nums[mid])
                l = mid + 1
        min_number = min(nums[l], nums[r], min_number)
        return min_number
                