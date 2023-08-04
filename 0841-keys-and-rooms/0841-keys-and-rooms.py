class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = set()
        queue = collections.deque()
        queue.append(0)
        visited.add(0)
        
        while queue:
            top = queue.popleft()
            top_row = rooms[top]
            
            for room in top_row:
                if room not in visited:
                    visited.add(room)
                    queue.append(room)
        
        return len(rooms) == len(visited)
        