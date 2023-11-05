class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        
        adj = collections.defaultdict(list)
        
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        # print(adj)
        children = collections.defaultdict(list)
        
        def getchildren(node, visited):
            
            visited.add(node)
            for child in adj[node]:
                if child not in visited:
                    children[node].append(child)
                    getchildren(child, visited)
        getchildren(0, set())
        # print(children)
        
        def backtrack(node):
            # You have two choices.
            if len(children[node]) == 0:
                # leaf node
                # print(node, [values[node], 0])
                return [values[node], 0]
            else:
                value1 = 0
                value2 = 0
                for child in children[node]:
                    res = backtrack(child)
                    value1 += res[0]
                    value2 += res[1]
                # print(node, [value1 + values[node], max(value2, value1)])
                return [value1 + values[node], max(value2 + values[node], value1)]
        ans = backtrack(0)
        # print(ans)
        return ans[1]
                    
                    
                    
            
        