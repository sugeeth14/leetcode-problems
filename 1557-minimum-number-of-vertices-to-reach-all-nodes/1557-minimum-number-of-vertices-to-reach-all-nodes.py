class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        borders = set()
        for edge in edges:
            borders.add(edge[1])
        
        res = []
        for i in range(n):
            if i not in borders:
                res.append(i)
        return res
        