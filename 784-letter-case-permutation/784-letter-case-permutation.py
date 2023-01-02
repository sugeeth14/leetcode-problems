class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # Consider it as a decision tree
        # We will do it using dp and build it bottom up so that we can cache results without repeating computation
        # So we have to iterate from behind and keep adding the results to get the final result
        
        # First seed the result with last character
        char = s[-1]
        res = []
        if char.isdigit():
            res.append(char)
        else:
            res.append(char.lower())
            res.append(char.upper())
        
        # With the seed of result ready start iterating from back.
        for i in range(len(s) -2, -1, -1):
            if s[i].isdigit():
                for j in range(len(res)):
                    res[j] = s[i] + res[j]
            else:
                # You have two choices here
                upper_char = s[i].upper()
                lower_char = s[i].lower()
                # Add the both characters
                new_res = []
                for r in res:
                    new_res.append(upper_char + r)
                    new_res.append(lower_char + r)
                res = new_res
        return res
            
        
        