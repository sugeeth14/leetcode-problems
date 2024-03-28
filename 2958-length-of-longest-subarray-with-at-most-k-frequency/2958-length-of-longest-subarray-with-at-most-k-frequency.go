func maxSubarrayLength(nums []int, k int) int {
    
    l := 0
    res := 0
    dic := map[int]int{}
    
    for i, num := range nums {
        dic[num]++
        for dic[num] > k {
            dic[nums[l]]--
            l++
        }
        window := i - l + 1
        res = max(res, window)
    }
    return res
    
}