class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        '''
        Algorithm:
        1. Make a dictionary of mod frequencies of k
        2. Then, iterate through each integer and find its mod, then see if there is a remining mod frequency element left to be added to 0
        3. If so subtract from the dict and continue
        4. If not return False
        5. If every element has return true at the end.
        '''
        
        dic = collections.defaultdict(int)
        
        for num in arr:
            dic[num % k] += 1
        
        
        
        # You can just iterate the dicts and tell
        for i in range(1, k):
            remaining = k - i
            if dic[remaining] == dic[i]:
                continue
            else:
                return False
        
        if dic[0] % 2 != 0:
            return False
        
        return True
        