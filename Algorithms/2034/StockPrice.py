import heapq

class StockPrice:

    def __init__(self):
        self.price_map = {}
        self.max_timestamp = 0
        self.min_price_heap, self.max_price_heap = [], []

    def update(self, timestamp: int, price: int) -> None:
        self.price_map[timestamp] = price
        self.max_timestamp = max(self.max_timestamp, timestamp)
        heapq.heappush(self.min_price_heap, (price, timestamp))
        heapq.heappush(self.max_price_heap, (-price, timestamp))

    def current(self) -> int:
        return self.price_map[self.max_timestamp]

    def maximum(self) -> int:
        while self.price_map[self.max_price_heap[0][1]] != -self.max_price_heap[0][0]:
            heapq.heappop(self.max_price_heap)
        return -self.max_price_heap[0][0]

    def minimum(self) -> int:
        while self.price_map[self.min_price_heap[0][1]] != self.min_price_heap[0][0]:
            heapq.heappop(self.min_price_heap)
        return self.min_price_heap[0][0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
