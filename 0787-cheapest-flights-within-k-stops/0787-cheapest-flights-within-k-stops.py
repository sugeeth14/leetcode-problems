class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        Algorithm:
        1. We will be doing this in BFS manner
        2. We will initialize a res variable to inf which holdest the cheapest price.
        3. We also create a queue to do the bfs.
        4. We initially add all the children of the source to the queue. With steps and cost
        5. We keep popping from the queue and if the child is not visited, we will visit its children.
        6. We will also visit if cost to reach a node is less than the existing cost
        6. Once we reach the destination we update the res
        7. We add the children only if the current cost is less than res.
        '''
        
        res = {}
        # initially every node is at a distance of inf from the source node. 
        for i in range(n):
            res[i] = float('inf')
        
        # update res from source to source as zero
        res[src] = 0
        
        queue = collections.deque()
        visited = set()
        
        # construct an adjacency matrix of children nodes.
        adj = collections.defaultdict(list)
        for flight in flights:
            adj[flight[0]].append([1, flight[1], flight[2]]) # add the flight to the adj list as children.
        
        # add the source flights children to the queue
        for child in adj[src]:
            queue.append(child)
        
        while queue:
            steps, stop, cost = queue.popleft()
            if stop in visited and cost >= res[stop]:
                # We need not do anything as this is the best possible way to reach the stop
                pass
            else:
                visited.add(stop) # The stop has been visited. 
                # update the res of the stop
                res[stop] = cost
                if steps == k + 1:
                    pass # Do nothing as we have aleady reached the maximum possible steps
                else:
                    # Go to the next level of bfs
                    for child in adj[stop]:
                        
                        queue.append([steps + 1, child[1], child[2] + res[stop]])
        if dst in visited:
            return res[dst]
        return -1
                
            
            
        