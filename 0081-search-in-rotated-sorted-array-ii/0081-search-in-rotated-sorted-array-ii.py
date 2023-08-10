class Solution:
    def search(self, nums: List[int], target: int) -> bool:


        l, r = 0, len(nums) - 1

        def binary_search(l, r):
            if l > r :
                return False
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            else:
                if target >= nums[mid] and target <= nums[r]:
                    l = mid + 1
                    return binary_search(l, r)
                elif target <= nums[mid] and target >= nums[l]:
                    r = mid - 1
                    return binary_search(l, r)
                else:
                    return binary_search(mid + 1, r) or binary_search(l, mid - 1)

        return (binary_search(l, r))

        