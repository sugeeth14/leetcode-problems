class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        sorted_strings = [""] * len(strs)
        for i in range(len(strs)):
            sorted_strings[i] = "".join(sorted(strs[i]))
        # print(strs)
        res = []
        dic = collections.defaultdict(list)
        
        for i in range(len(sorted_strings)):
            dic[sorted_strings[i]].append(strs[i])
        
        for key in dic:
            res.append(dic[key])
        return res