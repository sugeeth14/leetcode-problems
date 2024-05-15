class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        '''
        Algorithm:
        1. Precompute the positions
        2. Sort the array
        3. Place the elements of array in the precomputed positions
        '''
        queue = collections.deque()
        
        positions = []
        
        for i in range(len(deck)):
            queue.append(i)
        while queue:
            top = queue.popleft()
            positions.append(top)
            if not queue:
                break
            queue.append(queue.popleft())
        # print(positions)
        res = [0] * len(positions)
        deck.sort()
        for i in range(len(positions)):
            res[positions[i]] = deck[i]
        return res
            
        