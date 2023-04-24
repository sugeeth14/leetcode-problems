class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            # update it to the least recently used and then return it
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return - 1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            
            self.insert(self.cache[key])
            self.cache[key].value = value
        else:
            self.cache[key] = Node(key, value)
            if len(self.cache) > self.capacity:
                # remove the lru
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]
            self.insert(self.cache[key])
            
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)