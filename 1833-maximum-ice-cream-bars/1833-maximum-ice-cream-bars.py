class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        for i in range(len(costs)):
            coins -= costs[i]
            if coins >=0:
                res += 1
            else:
                return res
        return res
        