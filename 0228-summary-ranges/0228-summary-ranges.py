class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        start, end = nums[0], nums[0]
        res = []
        
        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = end + 1
            else:
                # we found the end of the range
                # print(start, end)
                if start == end:
                    res.append(str(end))
                else:
                    res.append(str(start) + "->" + str(end))
                # update new start and end
                start, end = nums[i], nums[i]
        if start == end:
            res.append(str(end))
        else:
            res.append(str(start) + "->" + str(end))
        return res
        