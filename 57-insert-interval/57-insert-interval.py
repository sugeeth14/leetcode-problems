class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # first append a dummy to the result
        if len(intervals) == 0:
            return [newInterval]
        inserted = False
        res = []
        for i in range(len(intervals)):
            if newInterval[0] <= intervals[i][0]:
                # Merge the new interval with previous before appending
                if not res:
                    res.append(newInterval)
                else:
                    if newInterval[0] <= res[-1][1]:
                        res[-1][1] = max(res[-1][1], newInterval[1])
                    else:
                        res.append(newInterval)
                inserted = True
                break
            else:
                res.append(intervals[i])
        
        # it will break at a certain i
        if not inserted:
            # It has not been merged
            if newInterval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], newInterval[1])
            else:
                res.append(newInterval)
            return res
        # print(res)
        while i < len(intervals):
            prevStart, prevEnd = res[-1][0], res[-1][1]
            if intervals[i][0] <= prevEnd:
                # There is overlap
                res[-1] = [prevStart, max(prevEnd, intervals[i][1])]
            else:
                res.append(intervals[i])
            i += 1
        return res
            
        