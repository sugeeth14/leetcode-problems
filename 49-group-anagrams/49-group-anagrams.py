class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for st in strs:
            sorted_st = "".join(sorted(st))
            if sorted_st in dic:
                dic[sorted_st].append(st)
            else:
                dic[sorted_st] = [st]
        # res = []
        res = dic.values()
        return res
        