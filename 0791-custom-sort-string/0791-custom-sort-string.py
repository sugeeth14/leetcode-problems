class Solution:
    def customSortString(self, order: str, s: str) -> str:
        '''
        Algorithm:
        1. Count the frequencies of each character in s
        2. Iterate through the order and append the number of character to the res.
        3. Return the res
        
        '''
        
        res = ""
        dic = collections.defaultdict(int)
        
        for char in s:
            dic[char] += 1
        for char in order:
            res = res + (dic[char] * char)
            dic[char] = 0
        for char in dic:
            if dic[char] != 0:
                res += (dic[char] * char)
        return res
        