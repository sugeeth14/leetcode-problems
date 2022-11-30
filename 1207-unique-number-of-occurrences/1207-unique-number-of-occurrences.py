class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import defaultdict
        dic = defaultdict(int)
        for i in range(len(arr)):
            dic[arr[i]] += 1
        
        seen = set()
        for key in dic:
            if dic[key] in seen:
                return False
            seen.add(dic[key])
        return True
        