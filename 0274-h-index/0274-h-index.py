class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        
        buckets = [0] * (len(citations) + 1)
        n = len(citations)
        
        # put in buckets based on the number of citations
        
        for c in citations:
            if c < n:
                buckets[c] += 1
            else:
                buckets[n] += 1
                
        count = 0
        
        
        for i in range(n, -1, -1):
            count = count + buckets[i]
            
            if count >= i:
                return i
        return 0