class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if target == nums[mid]:
                return mid
            elif nums[l] <= target <= nums[mid]:
                r = mid - 1
            elif nums[mid] <= target <= nums[r]:
                l = mid + 1
            elif target >= nums[mid]:
                if nums[mid] >= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # print("Came")
                if nums[mid] >= nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # print(l, r)
        return -1
        