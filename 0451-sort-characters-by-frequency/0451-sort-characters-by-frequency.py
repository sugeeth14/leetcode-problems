class Solution:
    def frequencySort(self, s: str) -> str:
        
        dic = {}
        
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i], 0) + 1
        
        res = ""
        sorted_dic = sorted(dic.items(), key=lambda x:x[1],reverse=True)
        
        for key, value in sorted_dic:
            res += (key*value)
        return res
        