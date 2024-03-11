func intersection(nums1 []int, nums2 []int) []int {
    /*
    Algorithm:
    1. Create a set for nums1
    2. Iterate over the second array nums2
    3. For each element in nums2 check if the element is in set 1
    4. If it is present add it to the result list
    5. Else discard
    6. Return the result list
    */
    
    set1 := map[int]bool{}
    
    for _, num := range(nums1){
        set1[num] = true
    }
    set2 := map[int]bool{}
    for _, num := range(nums2) {
        set2[num] = true
    }
    
    var res []int
    
    for k, _ := range(set2){
        if _, ok := set1[k]; ok{
            res = append(res, k)
        }
    }
    return res
    
    
}