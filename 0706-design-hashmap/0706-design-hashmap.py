class MyHashMap:

    def __init__(self):
        self.ans = [-1] * 1000001
        

    def put(self, key: int, value: int) -> None:
        self.ans[key] = value
        
        

    def get(self, key: int) -> int:
        return self.ans[key]
        

    def remove(self, key: int) -> None:
        self.ans[key] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)