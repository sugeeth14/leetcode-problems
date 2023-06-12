class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        final_list = []
        if len(nums) == 0:
            return []

        start = nums[0]
        end = nums[0]

        for num in nums[1:]:
            if end + 1 != num:
                if end == start:
                    final_list.append(str(end))
                else:
                    final_list.append(str(start) + "->" + str(end))
                start = num
                end = num
            else:
                end += 1

        if end == start:
            final_list.append(str(end))
        else:
            final_list.append(str(start) + "->" + str(end))

        return (final_list)

        