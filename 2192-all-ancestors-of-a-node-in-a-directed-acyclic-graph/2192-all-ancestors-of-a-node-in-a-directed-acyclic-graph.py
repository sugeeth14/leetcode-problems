class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        children = collections.defaultdict(list)
        
        for req in edges:
            children[req[0]].append(req[1])
        
        
        # print(chil)
        dic = collections.defaultdict(set)
        
        def topSort(node, visited):
            visited.add(node)
            res = set()
            res.add(node)
            # print(node, children[node])
            for child in children[node]:
                if child not in visited:
                    res = res | topSort(child, visited)
            
            dic[i] = res
            return dic[i]   
        
        
        for i in range(n):
            topSort(i, set())
            # print(dic[i])
        
        ans = collections.defaultdict(list)
        
        for i in range(n):
            for val in dic[i]:
                if val == i:
                    continue
                else:
                    ans[val].append(i)
        # print(ans)
        res = []
        for i in range(n):
            res.append(ans[i])
        return res