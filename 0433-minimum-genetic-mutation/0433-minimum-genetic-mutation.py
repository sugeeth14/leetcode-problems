class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # Algorithm
        # Add the start gene to a queue
        # look at all the genes in the bank and see if any of them is not visited and has just one difference
        # If so, check if it is equal to the end gene and if so return the level
        # If not equal to the end gene, mark it as visited and add it to the queue with an increased level
        # keep iterating until the queue is not empty
        # if still not found an answer return -1
        
        if startGene == endGene:
            return 0
        
        
        queue = collections.deque()
        visited = set()
        
        queue.append((startGene, 0))
        visited.add(startGene)
        
        def get_difference(str1, str2):
            count = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    count += 1
                    if count > 1:
                        return count
            return count
                
        
        while queue:
            top, level = queue.popleft()
            # Iterate through the bank and get the difference in positions
            for gene in bank:
                if gene not in visited:
                    difference = get_difference(top, gene)
                    if difference == 1:
                        if gene == endGene:
                            return level + 1
                        else:
                            visited.add(gene)
                            queue.append((gene, level + 1))
        return -1
                    
        