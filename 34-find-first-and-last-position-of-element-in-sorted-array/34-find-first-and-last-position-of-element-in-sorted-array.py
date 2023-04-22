class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        if target < nums[0] or target > nums[-1]:
            return [-1, -1]
        
        l = 0
        r = len(nums) - 1
        end = len(nums)
        while l <= r:
            mid = (l + r)//2
            if nums[mid] > target:
                end = min(end, mid)
                r = mid - 1
            elif nums[mid] == target:
                l = mid + 1
            else:
                l = mid + 1
        start = - 1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] < target:
                start = max(start, mid)
                l = mid + 1
            elif nums[mid] == target:
                r = mid - 1
            else:
                r = mid - 1
        # print(start, end)
        if nums[start + 1] != target or nums[end - 1] != target:
            return [-1, -1]
        return [start + 1, end - 1]
                
        