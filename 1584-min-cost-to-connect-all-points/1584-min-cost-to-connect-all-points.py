class Node:
    def __init__(self, p):
        self.point = p
        self.rank = 0
        self.parent = None
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = collections.defaultdict(list)
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                distances[distance].append([points[i], points[j]])
        # print(distances[3])
        
        node_map = {}
        
        for point in points:
            node_map[tuple(point)] = Node(point)
            node_map[tuple(point)].parent = node_map[tuple(point)]
        
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2:
                return False
            else:
                if parent1.rank == parent2.rank:
                    parent1.rank += 1
                    parent2.parent = parent1
                elif parent1.rank > parent2.rank:
                    parent2.parent = parent1
                else:
                    parent1.parent = parent2
                return True
        def find(node):
            if node.parent == node:
                return node.parent
            else:
                parent = find(node.parent)
                node.parent = parent
                return node.parent
        ans = 0
        
        for key in sorted(distances):
            for p in distances[key]:
                if union(node_map[tuple(p[0])], node_map[tuple(p[1])]):
                    ans += key
        return ans
        