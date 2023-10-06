class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1
        cache = {}
        cache[0] = 1
        cache[1] = 1
        cache[2] = 2
        cache[3] = 3
        for i in range(4,n+1):
            cache[i] = cache[i-1] * cache[1]
            for j in range(1,((i+1)//2) + 1):
                
                rem = i - j
                # print(j, rem)
                cache[i] = max(cache[i], cache[rem] * cache[j])
                # print(cache[i])
        return cache[n]
        