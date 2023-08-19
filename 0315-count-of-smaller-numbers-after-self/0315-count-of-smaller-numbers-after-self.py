from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        s = SortedList()
        # print(s)
        counts = [0] * len(nums)
        for i in range(len(nums) -1, -1, -1):
            counts[i] = s.bisect_left(nums[i])
            s.add(nums[i])
        return counts
            
        