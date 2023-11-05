class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        if k >= len(arr)-1:
            return max(arr)
        
            
        
        dic = collections.defaultdict(int)
        
        queue = collections.deque()
        
        for i in range(len(arr)):
            queue.append(arr[i])
        
        while True:
            top1, top2 = queue.popleft(), queue.popleft()
            if top1 > top2:
                dic[top1] += 1
                queue.appendleft(top1)
                queue.append(top2)
                if dic[top1] >= k:
                    return top1
            else:
                dic[top2] += 1
                queue.appendleft(top2)
                queue.append(top1)
                if dic[top2] >= k:
                    return top2
        