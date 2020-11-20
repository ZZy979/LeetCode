from collections import Counter

# 方法1：使用Counter
# track时间复杂度：O(1)，getRankOfNumber时间复杂度：O(k)，空间复杂度：O(k)，k为已出现过的不同数字的个数
# 232 ms
class StreamRank:

    def __init__(self):
        self.count = Counter()

    def track(self, x: int) -> None:
        self.count[x] += 1

    def getRankOfNumber(self, x: int) -> int:
        rank = 0
        for k in sorted(self.count):
            if k > x:
                break
            rank += self.count[k]
        return rank


# Your StreamRank object will be instantiated and called as such:
# obj = StreamRank()
# obj.track(x)
# param_2 = obj.getRankOfNumber(x)
