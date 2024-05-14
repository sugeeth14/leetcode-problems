class Solution:
    def reorganizeString(self, s: str) -> str:
        '''
        Algorithm:
        1. Create a frequency dict of each character. 
        2. Push the frequencies into a heap.
        3. Every time, keep popping the max element, if the element is same as previous one, pop another element.
        4. Reduce the value and push back to the heap.
        5. If the top character is equal and you cannot pop anymore from the heap return empty string. 
        
        6. Return the res at the end.
        '''
        
        heap = []
        
        heapq.heapify(heap)
        
        dic = collections.defaultdict(int)
        
        for char in s:
            dic[char] += 1
        
        for char in dic:
            heappush(heap, (-dic[char], char))
        
        res = ""
        while heap:
            value, char = heappop(heap)
            if res == "":
                res += char
                if value + 1 != 0:
                    heappush(heap, (value + 1, char))
            else:
                last_char = res[-1]
                if char != last_char:
                    res += char
                    if value + 1 != 0:
                        heappush(heap, (value + 1, char))
                else:
                    if len(heap) == 0:
                        return ""
                    second_value, second_char = heappop(heap)
                    res += second_char
                    heappush(heap, (value, char))
                    if second_value + 1 != 0:
                        heappush(heap, (second_value + 1, second_char))
        return res
        