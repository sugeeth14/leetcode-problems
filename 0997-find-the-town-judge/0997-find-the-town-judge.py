class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_others = set()
        count_trust = collections.defaultdict(int)
        
        for t in trust:
            trust_others.add(t[0])
            count_trust[t[1]] += 1
        
        for i in range(1, n + 1):
            if i not in trust_others and count_trust[i] == n-1:
                return i
        return -1