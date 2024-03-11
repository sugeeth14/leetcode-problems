func customSortString(order string, s string) string {
    /*
    Algorithm:
    1. Create a dictionary of counts for each character in s
    2. Iterate over the order and substitue the same number of character as string s into the result string and make the character count of s as zero
    3. Iteratere over all keys of s again and add to result whichever are not zero
    4. Return the res
    */
    
    dic := map[rune]int{}
    
    for _, char := range s{
        dic[char]++
    }
    
    res := ""
    for _, char := range order {
        if _, ok := dic[char]; ok {
            res += strings.Repeat(string(char), dic[char])
            dic[char] = 0
        }
    }
    for k, v := range dic {
        if v != 0 {
            res += strings.Repeat(string(k), v)
        }
    }
    return res
    
}