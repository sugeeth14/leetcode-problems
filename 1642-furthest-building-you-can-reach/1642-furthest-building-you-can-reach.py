class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        '''
        Algorithm:
        1. Create a heap.
        2. Keep adding difference to the heap. Add difference only if next one is greater height
        3. if the heap reaches size of ladders + 1 then pop an element which is hte min element.
        4. Subtract that element from bricks
        5. If bricks is less than 0 return the current result
        6. Else update the current result as the current index
        7. Return result at the end.
        '''
        h = []
        heapq.heapify(h)
        res = 0
        for i in range(1, len(heights)):
            if heights[i] > heights[i-1]:
                # Add the difference to heap
                heapq.heappush(h, heights[i] - heights[i-1])
                if len(h) == ladders + 1:
                    # out of ladders must use bricks
                    top = heapq.heappop(h)
                    # print(top)
                    bricks -= top
                    if bricks < 0:
                        return res
                    else:
                        res = i
                # print(bricks)
            res = i
        return res
        