from sortedcontainers import SortedDict

# 方法二：差分数组
# 时间复杂度O(n²)，空间复杂度O(n)
class MyCalendarTwo:

    def __init__(self):
        self.cnt = SortedDict()

    def book(self, startTime: int, endTime: int) -> bool:
        self.cnt[startTime] = self.cnt.get(startTime, 0) + 1
        self.cnt[endTime] = self.cnt.get(endTime, 0) - 1
        max_book = 0
        for c in self.cnt.values():
            max_book += c
            if max_book > 2:
                self.cnt[startTime] = self.cnt.get(startTime, 0) - 1
                self.cnt[endTime] = self.cnt.get(endTime, 0) + 1
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
