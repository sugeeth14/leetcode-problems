class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.rank = 0
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2:
                return
            else:
                if parent1.rank == parent2.rank:
                    parent1.rank += 1
                    parent2.parent = parent1
                elif parent1.rank > parent2.rank:
                    parent2.parent = parent1
                else:
                    parent1.parent = parent2
        
        def find(node):
            if node.parent == node:
                return node.parent
            else:
                parent = find(node.parent)
                node.parent = parent
                return node.parent
        
        node_map = {}
        for i in range(len(source)):
            node_map[i] = Node(i)
            node_map[i].parent = node_map[i]
        
        for swap in allowedSwaps:
            union(node_map[swap[0]], node_map[swap[1]])
        
        clusters = []
        
        for i in range(len(source)):
            parent = find(node_map[i])
            clusters.append(parent.data)
        # print(clusters)
        dic = {}
        for i in range(len(clusters)):
            if clusters[i] not in dic:
                dic[clusters[i]] = collections.defaultdict(int)
            dic[clusters[i]][source[i]] += 1
        # print(dic)
        res = 0
        for i in range(len(source)):
            # if source[i] == target[i]:
            #     pass
            # else:
            if target[i] in dic[clusters[i]] and dic[clusters[i]][target[i]] != 0:
                dic[clusters[i]][target[i]] -= 1
            else:
                res += 1
        return res
        