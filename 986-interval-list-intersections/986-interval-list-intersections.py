class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ptr1 = 0
        ptr2 = 0
        res = []
        while ptr1 < len(firstList) and ptr2 < len(secondList):
            interval1 , interval2 = firstList[ptr1], secondList[ptr2]
            # check if any overalap
            if interval1[0] <= interval2[0] <= interval1[1] or interval2[0] <= interval1[0] <= interval2[1]:
                res.append([max(interval1[0], interval2[0]), min(interval1[1], interval2[1])])
            if interval1[1] > interval2[1]:
                ptr2 += 1
            else:
                ptr1 += 1
        return res
                
        