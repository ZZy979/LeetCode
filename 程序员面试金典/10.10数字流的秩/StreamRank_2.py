import bisect

# 方法2：使用bisect模块
# track时间复杂度：O(n)，getRankOfNumber时间复杂度：O(log n)，空间复杂度：O(n)
# 76 ms
class StreamRank:

    def __init__(self):
        self.l = []

    def track(self, x: int) -> None:
        bisect.insort_left(self.l,x)

    def getRankOfNumber(self, x: int) -> int:
        return bisect.bisect_right(self.l, x)


# Your StreamRank object will be instantiated and called as such:
# obj = StreamRank()
# obj.track(x)
# param_2 = obj.getRankOfNumber(x)
