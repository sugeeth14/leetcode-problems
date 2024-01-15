class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        dic = {}
        
        for match in matches:
            dic[match[1]] = dic.get(match[1], 0) + 1
            dic[match[0]] = dic.get(match[0], 0)
        
        ans1 = []
        ans2 = []
        for key in sorted(dic):
            if dic[key] == 0:
                ans1.append(key)
            elif dic[key] == 1:
                ans2.append(key)
            else:
                pass
        
        return [ans1, ans2]
        