from sortedcontainers import SortedList

class StockPrice:

    def __init__(self):
        self.price_map = {}
        self.max_timestamp = 0
        self.prices = SortedList()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.price_map:
            self.prices.discard(self.price_map[timestamp])
        self.prices.add(price)
        self.price_map[timestamp] = price
        self.max_timestamp = max(self.max_timestamp, timestamp)

    def current(self) -> int:
        return self.price_map[self.max_timestamp]

    def maximum(self) -> int:
        return self.prices[-1]

    def minimum(self) -> int:
        return self.prices[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
