class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Algorithm: We will be using Topological sort
        # Initialize visited set and dic to keep track of parents of each node
        # iterate over each nodes and call top sort on that node if that node doesn't have any incoming edges and it is not visited.
        # during every step before calling the children, populate the dic for the current node and add the current node to the set and call for its children.
        # Once all the children have been visited just return. 
        # At the end you will have  a dic of set that can be used for a simple look up for queries.
        
        children = collections.defaultdict(list)
        parents = collections.defaultdict(list)
        
        for req in prerequisites:
            children[req[0]].append(req[1])
            parents[req[1]].append(req[0])
        
        
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