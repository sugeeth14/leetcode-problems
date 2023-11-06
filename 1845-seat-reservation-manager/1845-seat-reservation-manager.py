class SeatManager:

    def __init__(self, n: int):
        self.seats = []
        heapq.heapify(self.seats)
        # print(self.seats)
        for i in range(1, n+ 1):
            heappush(self.seats, i)
        # print(self.seats)
        

    def reserve(self) -> int:
        top = heappop(self.seats)
        return top
        

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.seats, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)