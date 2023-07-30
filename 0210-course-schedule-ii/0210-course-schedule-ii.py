class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
        
        res = []
        visited = set()
        dic = {}
        for i in range(numCourses):
            dic[i] = []
        
        done = {}
        
        for req in prerequisites:
            dic[req[0]].append(req[1])
        
        # print(dic)
        
        def backtrack(node):
            if node in visited:
                return False
            else:
                # add it to visited
                visited.add(node)
                # visit all its children
                for child in dic[node]:
                    if child in done:
                        continue
                    if not backtrack(child):
                        # there is a cycle return False
                        return False
                # After visiting all the children add the current course to the result
                done[node] = True
                res.append(node)
                return True
        
        for i in range(numCourses):
            if i not in visited and len(dic[i]) != 0:
                # print(i)
                if not backtrack(i):
                    return []
        for i in range(numCourses):
            if i not in visited:
                res.append(i)
        return res
        