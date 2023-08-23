class Solution:
    def reorganizeString(self, s: str) -> str:
        queue = collections.deque()
        
        h = []
        heapq.heapify(h)
        
        dic = collections.defaultdict(int)
        
        for char in s:
            dic[char] += 1
        
        for key in dic:
            heapq.heappush(h, [-dic[key],key])
        # print(h)
        res = ""
        
        count, top = heapq.heappop(h)
        res += top
        count += 1
        # print(res)
        # heapq.heappush(h, [top, count])
        while h:
            new_count, new_top = heapq.heappop(h)
            if new_count == 0:
                break
            else:
                res += new_top
                new_count += 1
                heapq.heappush(h, [count,top])
                top = new_top
                count = new_count
        # print(res)
        if count == 1 and res[-1] != top:
            res += top
        if len(res) == len(s):
            return res
        else:
            return ""
            
        
        
        