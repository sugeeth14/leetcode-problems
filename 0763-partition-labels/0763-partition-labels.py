class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = collections.defaultdict(int)
        
        for i in range(len(s)):
            last_index[s[i]] = i
        
        # print(last_index)
        i = 0
        j = 0
        # res = [-1]
        res = []
        while i < len (s) and i <= j:
            char = s[i]
            if last_index[char] <= j:
                pass
            else:
                
                j = last_index[char]
            if i == j:
                if res:
                    res.append(i)
                else:
                    res.append(i+1)
                i += 1
                j += 1
            else:
                i += 1
        # return res
        # for i in range(1, len(res)):
        #     res[i] = res[i] - res[i-1]
        final = [res[0]]
        for i in range(1, len(res)):
            final.append(res[i]-res[i-1])
            if i == 1:
                final[-1] += 1
        return final
            
                
        