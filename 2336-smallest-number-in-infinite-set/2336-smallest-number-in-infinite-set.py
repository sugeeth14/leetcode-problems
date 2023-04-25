class SmallestInfiniteSet:

    def __init__(self):
        self.removed = {}
        

    def popSmallest(self) -> int:
        i = 1
        while True:
            if i not in self.removed:
                break
            else:
                i += 1
        self.removed[i] = True
        return i
        

    def addBack(self, num: int) -> None:
        if num in self.removed:
            del self.removed[num]
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)