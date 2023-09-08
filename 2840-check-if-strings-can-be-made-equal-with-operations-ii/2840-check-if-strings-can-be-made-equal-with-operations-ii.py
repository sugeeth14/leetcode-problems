class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1_odd = collections.defaultdict(int)
        s1_even = collections.defaultdict(int)
        
        s2_odd = collections.defaultdict(int)
        s2_even = collections.defaultdict(int)
        
        for i in range(len(s1)):
            if i % 2 == 0:
                s1_odd[s1[i]] += 1
                s2_odd[s2[i]] += 1
            else:
                s1_even[s1[i]] += 1
                s2_even[s2[i]] += 1
        
        for i in range(97,123):
            if s1_odd[chr(i)] != s2_odd[chr(i)] or s1_even[chr(i)] != s2_even[chr(i)]:
                return False
        return True
        