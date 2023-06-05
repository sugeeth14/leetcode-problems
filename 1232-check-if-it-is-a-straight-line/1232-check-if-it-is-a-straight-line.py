class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        point1 = coordinates[0]
        point2 = coordinates[1]
        
        if point1[0] == point2[0]:
            slope = "inf"
        else:
            slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
            
        ans = True
        
        for i in range(2, len(coordinates)):
            point = coordinates[i]
            if slope == "inf":
                if point[0] != point1[0]:
                    return False
            else:
                if point[0] == point1[0]:
                    return False
                new_slope = (point[1] - point1[1]) / (point[0] - point1[0])
                if new_slope != slope:
                    return False
        return True