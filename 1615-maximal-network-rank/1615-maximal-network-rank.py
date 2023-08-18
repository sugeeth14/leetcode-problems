class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # roads_set = set(roads)
        roads_set = set()
        
        count_dic = collections.defaultdict(int)
        for start, end in roads:
            count_dic[start] += 1
            count_dic[end] += 1
            roads_set.add((start, end))
        maximum = 0
        
        for i in range(n):
            for j in range(i+1, n):
                current = count_dic[i] + count_dic[j]
                
                if (i, j) in roads_set or (j, i) in roads_set:
                    current -= 1
                maximum = max(current, maximum)
        return maximum
        
        