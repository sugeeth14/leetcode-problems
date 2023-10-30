class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        
        def get_bits(num):
            count = 0
            while num:
                count = count + (num & 1)
                num >>= 1
            return count
        
        def mysort(a, b):
            abits = get_bits(a)
            bbits = get_bits(b)
            
            if abits < bbits:
                return -1
            elif abits == bbits:
                if a <= b:
                    return -1
                else:
                    return 1
            else:
                return 1
        
        arr.sort(key=functools.cmp_to_key(mysort))
        return arr
        