class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        effective = [0] * len(gas)
        
        for i in range(len(gas)):
            effective[i] = gas[i] - cost[i]
        
        if sum(effective) < 0:
            return -1
        
        effective = effective + effective
        
        max_ans = -1
        max_index = -1
        for i in range(len(effective) - 1, -1, -1):
            effective[i] = max(0, effective[i] + (effective[i+1] if i + 1 < len(effective) else 0))
            if effective[i] >= max_ans:
                max_ans = effective[i]
                max_index = i
        return max_index % len(gas)
        