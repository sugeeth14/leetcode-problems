class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        
        def findpos(val):
            l = 0
            r = len(citations) - 1

            while l <= r:
                mid = (l + r)//2
                if citations[mid] > val:
                    r = mid - 1
                elif citations[mid] == val:
                    r = mid - 1
                else:
                    l = mid + 1

            return l
        
        l = 0
        r = max(citations)
        ans = 0
        
        while l <= r:
            mid = (l + r) // 2
            
            position = findpos(mid)
            # print(position)
            
            papers = len(citations) - position
            
            if papers > mid:
                ans = mid
                l = mid + 1
            elif papers == mid:
                return mid
            else:
                r = mid - 1
        return ans