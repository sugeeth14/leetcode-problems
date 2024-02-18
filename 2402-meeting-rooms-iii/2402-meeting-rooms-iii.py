class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        '''
        Algorithm:
        1. Sort the meetings by the start time.
        2. Initialize heap from 0 to n-1 with a list of start time as 0 and second element in the list as index from 0 to n - 1
        3. Also initialize a dictionary to maintain the count of the meetings held in a room.
        4. Iterate over each meeting, pop the top from the heap and add the end time - start time to the first index of the top of the heap. 
        5. Before pushing back update the dictionary
        6. Push back into the heap.
        7. At the end iterate over the dictionary and find the index with the maximum value and return the index.
        '''
        meetings.sort()
        # print(meetings)
        heap = []
        
        for i in range(n):
            heapq.heappush(heap, [0, i])
        
        dic = {}
        
        for start, end in meetings:
            top = heapq.heappop(heap)
            while start > top[0]:
                top[0] = start
                heapq.heappush(heap, top)
                top = heapq.heappop(heap)
            
            top[0] = top[0] + (end - start)
                
            # update the dictionary
            dic[top[1]] = dic.get(top[1],0) + 1
            heapq.heappush(heap, top)
        
        val = 0
        index = 0
        # print(dic)
        for i in range(n):
            if i in dic and dic[i] > val:
                index = i
                val = dic[i]
        return index
        