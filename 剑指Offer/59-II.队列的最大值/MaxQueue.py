from collections import deque

class MaxQueue:

    def __init__(self):
        self.data = deque()
        self.max_data = deque()

    def max_value(self) -> int:
        return self.max_data[0] if self.data else -1

    def push_back(self, value: int) -> None:
        self.data.append(value)
        while self.max_data and self.max_data[-1] < value:
            self.max_data.pop()
        self.max_data.append(value)

    def pop_front(self) -> int:
        if not self.data:
            return -1
        if self.data[0] == self.max_data[0]:
            self.max_data.popleft()
        return self.data.popleft()


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
