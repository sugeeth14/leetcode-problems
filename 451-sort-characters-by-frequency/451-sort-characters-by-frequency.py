class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import defaultdict
        dic = defaultdict(int)
        for char in s:
            dic[char] += 1
        
#         def my_cmp(a, b):
#             if dic[b] > dic[a]:
#                 return 1
#             else:
#                 return -1
            
        
#         sorted_string = sorted(s, key=functools.cmp_to_key(my_cmp))
#         return ("".join(sorted_string))
        temp = sorted(dic, key=dic.get, reverse=True)
        res = ""
        for char in temp:
            res += (char) * dic[char]
        return(res)
        
        
        