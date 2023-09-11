class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        
        for i in range(len(groupSizes)):
            dic[groupSizes[i]].append(i)
        # print(dic)
        res = []
        for key in dic:
            temp = []
            for i in range(len(dic[key])):
                temp.append(dic[key][i])
                if (i + 1) % key == 0:
                    res.append(temp)
                    temp = []
        return res
                    
        