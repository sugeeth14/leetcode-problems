func findMinArrowShots(points [][]int) int {
    /*
    Algorithm:
    1. Sort the points by the first index
    2. Maintain a res initialized to 1 to count the baloons.
    3. Start by maintaining an intersection which is equal to the start and end of the first value in points.
    4. Start iterating from the second index, if there is intersection, update the intersection, and continue
    5. If there is no intersection, add one to the res and make the new intersection equal to the start and end of the current point. 
    6. Return the res at the end.
    */
    
    // 1. Sorting the points using a comparator function
    sort.SliceStable(points, func(i, j int) bool {return points[i][0] < points[j][0]})
    
    //2. Initializing a variable called res to maintain the number of arrows
    res := 1 // Initialized to 1 for accounting the first index in points. 
    
    //3. The lower and upper bounds of intersection are x and y respectively.
    x, y := points[0][0], points[0][1]
    
    //4. Starting to iterate from second index
    for i := 1; i < len(points); i++ {
        if points[i][0] <= y {
            // There is an intersection update x, y
            x = max(x, points[i][0])
            y = min(y, points[i][1])
        } else {
            // 5. There is no intersection create a new bound for intersection
            res++
            x, y = points[i][0], points[i][1]
        }
        
    }
    
    // 6. Returning the res at the end.
    return res
    
}