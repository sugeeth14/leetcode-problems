class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        
        cache = {}
        mod = 1000000007
        def backtrack(current_n, current_m, current_k):
            if (current_n, current_m, current_k) in cache:
                return cache[(current_n, current_m, current_k)] % mod
            # print(current_n, current_m, current_k)
            rem_n = n - current_n
            rem_m = m - current_m
            rem_k = k - current_k
            if rem_m < rem_k:
                cache[(current_n, current_m, current_k)] = 0
                # print(0)
                return 0
            elif rem_n < rem_k:
                # print(0)
                cache[(current_n, current_m, current_k)] = 0
                return 0
            elif rem_n == 0 and rem_k == 0:
                # print(1)
                cache[(current_n, current_m, current_k)] = 1
                return 1
            elif rem_n == 0:
                # print(0)
                cache[(current_n, current_m, current_k)] = 0
                return 0
            else:
                # We have two choices either to increment the number or add the current number itself
                val = backtrack(current_n + 1, current_m, current_k) % mod
                for j in range(1, m +1):
                    if j > current_m:
                        val += (backtrack(current_n + 1, j, current_k + 1)%mod)
                        val %= mod
                    else:
                        if j != current_m:
                            val += (backtrack(current_n + 1, current_m, current_k)%mod)
                            val %= mod
                cache[(current_n, current_m, current_k)] = val%mod
                # print("backtrack", current_n, current_m, current_k,val)
                return val%mod
        
        res = 0
        for i in range(1, m+1):
        
            res += (backtrack(1, i, 1)%mod)
            res %= mod
        return res%mod
        