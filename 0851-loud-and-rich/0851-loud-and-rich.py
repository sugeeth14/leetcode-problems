class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        
        children = collections.defaultdict(list)
        
        for rich in richer:
            children[rich[1]].append(rich[0])
        # print(children)
        
        cache = {}
        def topSort(node, visited):
            if node in cache:
                return cache[node]
            else:
                visited.add(node)
                res = quiet[node]
                index = node
                for child in children[node]:
                    child_res = topSort(child, visited)
                    if child_res[0] < res:
                        res = child_res[0]
                        index = child_res[1]
                cache[node] = [res, index]
                return cache[node]
        
        for i in range(len(quiet)):
            topSort(i, set())
            
        ans = []
        for i in range(len(quiet)):
            ans.append(cache[i][1])
        return ans
            
                    
            
        