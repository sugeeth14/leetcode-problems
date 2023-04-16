class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        current_start, current_end = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start <= current_end:
                current_end = max(current_end, end)
            else:
                # Append to the result and start fresh
                res.append([current_start, current_end])
                current_start, current_end = start, end
                
        res.append([current_start, current_end])
        return res
        