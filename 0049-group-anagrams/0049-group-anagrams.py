class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Algorithm:
        1. Sort each word in str
        2. Iterate over each word if the word is already in dictionary add to the list in that dictionary key
        3. If not create an empty list with and the word into the list and as the key.
        '''
        
        sorted_strs = []
        for i in range(len(strs)):
            sorted_strs.append("".join(sorted(strs[i])))
        
        dic = {}
        
        for i in range(len(strs)):
            if sorted_strs[i] in dic:
                dic[sorted_strs[i]].append(strs[i])
            else:
                dic[sorted_strs[i]] = [strs[i]]
        return dic.values()
        