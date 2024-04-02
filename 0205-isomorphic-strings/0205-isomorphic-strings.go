func isIsomorphic(s string, t string) bool {
    /*
    Algorithm:
    1. Maintain a set of used characters that were already taken
    2. Also maintain a map of characters to know which characters are mapped
    */
    
    seen := map[byte]bool{}
    
    mapping := map[byte]byte{}
    for i := range s{
        if val, ok := mapping[s[i]]; ok {
            // It is present
            if val != t[i]{
                return false
            }
        } else {
            if _, ok := seen[t[i]]; ok{
                return false
            } else {
                seen[t[i]] = true
                mapping[s[i]] = t[i]
            }
        }
    }
    return true
    
}