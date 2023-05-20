class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        # print(adj)
        ans_dp = {}
        vertices = set()
        for i in range(len(equations)):
            numerator, denominator = equations[i][0], equations[i][1]
            vertices.add(numerator)
            vertices.add(denominator)
            ans_dp[(numerator, denominator)] = values[i]
            ans_dp[(denominator, numerator)] = 1/(values[i])
            # Also fill the adj matrix
            adj[numerator].append(denominator)
            adj[denominator].append(numerator)
            # adj[ord(numerator) - ord("a")][ord(denominator) - ord("a")] = 1
            # adj[ord(denominator) - ord("a")][ord(numerator) - ord("a")] = 1
        # print(adj)
        
        # now we need the backtrack function
        def backtrack(numerator, denominator, visited):
            if (numerator, denominator) in ans_dp:
                return ans_dp[(numerator, denominator)]
            if numerator in visited:
                return -1
            # try to find if the numerator and denominator could be linked
            visited.add(numerator)
            for i in range(len(adj[numerator])):
                # if adj[ord(numerator) - ord("a")][i] == 1:
                val = backtrack(adj[numerator][i], denominator, visited)
                if val != -1:
                    ans_dp[(numerator, denominator)] = ans_dp[(numerator,adj[numerator][i])] * val
                    visited.remove(numerator)
                    return ans_dp[(numerator, denominator)]
            visited.remove(numerator)
            ans_dp[(numerator, denominator)] = -1
            return ans_dp[(numerator, denominator)]                    
            
            
        
        res = []
        for query in queries:
            numerator, denominator = query[0], query[1]
            visited = set()
            res.append(backtrack(numerator, denominator, visited))
        return res
            
        