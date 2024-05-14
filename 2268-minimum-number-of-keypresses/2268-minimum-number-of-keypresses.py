class Solution:
    def minimumKeypresses(self, s: str) -> int:
        '''
        Algorithm:
        1. Calculate the frequencies of each character. 
        2. Sort the dictionary by values.
        3. Once sorted, iterate through the ordered dict or you can use a heap also.
        4. For the first 9 add 1 and next 9 add two to the result and so on.
        '''
        
        res = 0
        
        dic = collections.defaultdict(int)
        for char in s:
            dic[char] += 1
        
        count = 1
        for key in sorted(dic, key=dic.get, reverse=True):
            if count <= 9:
                res = res + dic[key]
            elif count <= 18:
                res = res + dic[key] * 2
            else:
                res = res + dic[key] * 3
            count += 1
        return res
            