class Solution:
    def maxLength(self, arr: List[str]) -> int:
        '''
        Algorithm:
        1. At every stage you have two choices, either to add the string arr[i] to the overall string or to not add it.
        2. When you add, you try to compute the best res by adding it and when you don't add you have another best result you compute.
        3. You compare both of them and get the best. 
        4. At the end you return the best value for the overall array.
        '''
        charSet = set()
        
        # now to the helper function overlap
        
        def overlap(s):
            combined_set = set(s) | charSet
            return len(combined_set) != len(s) + len(charSet)
        
        
        
        
        
        def backtrack(i):
            # backtrack at index i
            if i == len(arr):
                # we have reached the end no more elements to add, so we just return whatever result we have computed so far in this path.
                return len(charSet)
            
            res = 0
            if not overlap(arr[i]):
                # there is no overlap, so you can try and add this and see if this gives the best res
                for char in arr[i]:
                    charSet.add(char)
                res = backtrack(i + 1) # you have updated charset, now go to the next index to see what is the best res this gives.
                
                for char in arr[i]:
                    charSet.remove(char) # remove it for next set of backtracking.
                    
            return max(res, backtrack(i+1)) # compare it with the case when you don't add the current index arr[i] to the string
        
        return backtrack(0)
                    
                