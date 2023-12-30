class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dic = collections.defaultdict(int)
        
        for word in words:
            for char in word:
                dic[char] += 1
        
        for char in dic:
            if dic[char] % len(words) != 0:
                return False
        return True
        