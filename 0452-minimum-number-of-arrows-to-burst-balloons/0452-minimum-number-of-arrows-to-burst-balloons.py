class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        Algorithm:
        1. Sort the points by the first index
        2. Maintain a res initialized to 0 to count the baloons.
        3. Start by maintaining an intersection which is equal to the start and end of the first value in points.
        4. Start iterating from the second index, if there is intersection, update the intersection, and continue
        5. If there is no intersection, add one to the res and make the new intersection equal to the start and end of the current point. 
        6. Return the res at the end.    
        '''
        points.sort()
        
        res = 1
        x, y = points[0][0], points[0][1]
        
        for i in range(1, len(points)):
            if points[i][0] <= y:
                # There is an intersection update x, y
                x = max(points[i][0], x)
                y = min(points[i][1], y)
            else:
                # there is no intersection
                res += 1
                x, y = points[i][0], points[i][1]
        return res
            