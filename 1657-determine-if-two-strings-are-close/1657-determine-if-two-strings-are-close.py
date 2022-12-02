class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # There are two cases first all characters should be same
        # Second numbers should be equal
        if len(word1) != len(word2):
            return False
        from collections import defaultdict
        dic_1 = defaultdict(int)
        dic_2 = defaultdict(int)
        
        set_1 = set()
        set_2 = set()
        
        for char in word1:
            set_1.add(char)
            dic_1[char] += 1
        for char in word2:
            set_2.add(char)
            dic_2[char] += 1
        if set_1 != set_2:
            return False
        counts_1 = []
        counts_2 = []
        for char1, char2 in zip(dic_1, dic_2):
            counts_1.append(dic_1[char1])
            counts_2.append(dic_2[char2])
        counts_1.sort()
        counts_2.sort()
        return counts_1 == counts_2
            
            
        