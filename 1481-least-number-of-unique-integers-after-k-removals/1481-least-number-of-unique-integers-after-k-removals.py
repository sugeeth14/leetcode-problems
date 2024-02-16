class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = {}
        for num in arr:
            dic[num] = dic.get(num, 0) + 1
        
        
        for key, value in sorted(dic.items(), key=lambda item:item[1]):
            # print(key, value)
            if value > k:
                break
            else:
                k -= value
                value = 0
                
                dic[key] = 0
        count = 0
        # print(dic)
        for key in dic:
            if dic[key] != 0:
                count += 1
        return count