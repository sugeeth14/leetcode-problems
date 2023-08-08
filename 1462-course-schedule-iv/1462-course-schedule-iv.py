class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        children = collections.defaultdict(list)
        
        for req in prerequisites:
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
        
        
        for i in range(numCourses):
            topSort(i, set())
            # print(dic[i])
        
        # print(dic)
        ans = []
        for query in queries:
            if query[1] in dic[query[0]]:
                ans.append(True)
            else:
                ans.append(False)
        return ans