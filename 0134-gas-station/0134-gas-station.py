class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        diff = [0] * len(gas)
        
        for i in range(len(gas)):
            diff[i] = gas[i] - cost[i]
        if sum(diff) < 0:
            return -1
        
        diff = diff + diff
        
        
        ans = 0
        max_value = 0
        for i in range(len(diff) - 1, -1, -1):
            diff[i] = max(0, diff[i] + (diff[i+1] if i + 1 < len(diff) else 0))
            if diff[i] > max_value:
                max_value = diff[i]
                ans = i
        return ans %  (len(gas))
            
        