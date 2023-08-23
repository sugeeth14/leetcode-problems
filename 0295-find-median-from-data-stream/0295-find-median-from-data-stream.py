from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.arr = SortedList()
        

    def addNum(self, num: int) -> None:
        self.arr.add(num)
        

    def findMedian(self) -> float:
        if len(self.arr) % 2 != 0:
            return self.arr[len(self.arr)//2]
        else:
            # print(self.arr)
            return (self.arr[len(self.arr)//2] + self.arr[(len(self.arr)//2) - 1])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()