class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        # min_array = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            cost[i] = min(cost[i-1], cost[i-2]) + cost[i]
        res = min(cost[len(cost) -1], cost[len(cost)-2])
        return res
            