class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
class LUPrefix:

    def __init__(self, n: int):
        self.node_map = {}
    
    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return
        else:
            if parent1.data >= parent2.data:
                parent2.parent = parent1
            else:
                parent1.parent = parent2
    
    def find(self, node):
        if node.parent == node:
            return node.parent
        else:
            parent = self.find(node.parent)
            node.parent = parent
            return node.parent
        

    def upload(self, video: int) -> None:
        if video in self.node_map:
            return
        else:
            # Now we try to union
            self.node_map[video] = Node(video)
            self.node_map[video].parent = self.node_map[video]
            if video + 1 in self.node_map:
                self.union(self.node_map[video], self.node_map[video + 1])
            if video - 1 in self.node_map:
                self.union(self.node_map[video], self.node_map[video-1])
            
        

    def longest(self) -> int:
        if 1 not in self.node_map:
            return 0
            
            
        parent = self.find(self.node_map[1])
        return parent.data
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()