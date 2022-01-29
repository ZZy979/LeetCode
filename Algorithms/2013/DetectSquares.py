class DetectSquares:

    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x0, y0 = point
        return sum(self.points[x, y] * self.points[x0, y] * self.points[x, y0] for x, y in self.points if abs(x - x0) == abs(y - y0) and x != x0)


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
