from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.window = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.window.append(val)
        self.window_sum += val
        if len(self.window) > self.size:
            self.window_sum -= self.window.popleft()
        return self.window_sum / len(self.window)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
